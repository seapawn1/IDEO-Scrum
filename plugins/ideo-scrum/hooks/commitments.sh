#!/bin/sh
# IDEO-Scrum: put the commitments written in this project's logs into Claude's context.
#
# Runs on SessionStart and UserPromptSubmit (see hooks.json). It reads the commitments -- the Product,
# the Product Goal, and the Sprint Goal or design goal of the log that is open -- and prints them as
# plain text; Claude Code adds that text to the model's context.
#
# How it reads the logs (the rules are in convention 17 of `overview.md` in the scrum-kernel skill):
#   - a commitment is a one-row table whose first cell is `Commitment` (`承诺` in a Chinese log); the
#     second cell is the exact text;
#   - the nearest heading above it says which one it is: Product, Product Goal (product log,
#     `scrum/ProductBacklog.md`), Sprint Goal (`scrum/sprint-*/SprintBacklog.md`), Design goal
#     (`scrum/design-*/DesignBacklog.md`).
#   - a Sprint or design counts as open while its folder is under `scrum/`; two or more open Sprints
#     (or designs) are reported as a count, not by their goals, because the working copy has no single
#     current one.
#
# It prints nothing, and always exits 0, when anything is missing or goes wrong: no product log, a file it
# cannot read, a tool that is not installed. To switch it off, set IDEO_SCRUM_COMMITMENTS=off (in the
# "env" of a settings file, or in the shell).
#
# POSIX sh and awk, sed, tr, cksum, dirname, basename, mkdir only.

[ "$IDEO_SCRUM_COMMITMENTS" = "off" ] && exit 0

# Walk up from $1 until a directory holds scrum/ProductBacklog.md; print it.
find_root() {
  d=$(printf '%s' "$1" | tr '\\' '/')
  i=0
  while [ -n "$d" ] && [ "$i" -lt 64 ]; do
    if [ -f "$d/scrum/ProductBacklog.md" ]; then
      printf '%s' "$d"
      return 0
    fi
    parent=$(dirname "$d")
    [ "$parent" = "$d" ] && break
    d=$parent
    i=$((i + 1))
  done
  return 1
}

# Print "kind<TAB>key<TAB>text" for each commitment in the log $1 (the first one of each kind).
read_commitments() {
  tr -d '\r' < "$1" | awk '
    /^#/ { heading = $0; next }
    /^\|[ \t]*(承诺|Commitment)[ \t]*\|/ {
      key = $0
      sub(/^\|[ \t]*/, "", key)
      sub(/[ \t]*\|.*$/, "", key)
      text = $0
      sub(/^\|[ \t]*(承诺|Commitment)[ \t]*\|[ \t]*/, "", text)
      sub(/[ \t]*\|[ \t]*$/, "", text)
      kind = ""
      if (heading ~ /Sprint Goal/) kind = "sprint"
      else if (heading ~ /Product Goal/) kind = "productgoal"
      else if (heading ~ /Design [Gg]oal|设计目标/) kind = "design"
      else if (heading ~ /Product|产品/) kind = "product"
      if (kind != "" && !(kind in seen)) {
        seen[kind] = 1
        printf "%s\t%s\t%s\n", kind, key, text
      }
    }'
}

# field "<lines>" <kind> <column>: one column of the line of that kind.
field() {
  printf '%s\n' "$1" | awk -F'\t' -v k="$2" -v c="$3" '$1 == k { print $c; exit }'
}

# Print the text unless it is empty or an unfilled template placeholder such as <Sprint Goal>.
clean() {
  case $1 in
    '' | '<'*'>') return 1 ;;
  esac
  printf '%s' "$1"
}

main() {
  input=$(cat | tr -d '\r\n')
  meta=${input%%\"prompt\"*}
  event=$(printf '%s' "$meta" | sed -n 's/.*"hook_event_name" *: *"\([A-Za-z]*\)".*/\1/p')
  session=$(printf '%s' "$meta" | sed -n 's/.*"session_id" *: *"\([A-Za-z0-9_-]*\)".*/\1/p')
  source=$(printf '%s' "$meta" | sed -n 's/.*"source" *: *"\([a-z]*\)".*/\1/p')
  case $event in
    SessionStart | UserPromptSubmit) ;;
    *) return 0 ;;
  esac

  root=$(find_root "$PWD") || root=$(find_root "$CLAUDE_PROJECT_DIR") || return 0

  prod=$(read_commitments "$root/scrum/ProductBacklog.md")
  product=$(clean "$(field "$prod" product 3)")
  goal=$(clean "$(field "$prod" productgoal 3)")
  [ -n "$product$goal" ] || return 0
  key=$(field "$prod" product 2)
  [ -n "$key" ] || key=$(field "$prod" productgoal 2)

  n_sprints=0
  sprint_file=
  for f in "$root"/scrum/sprint-*/SprintBacklog.md; do
    [ -f "$f" ] || continue
    n_sprints=$((n_sprints + 1))
    sprint_file=$f
  done
  n_designs=0
  design_file=
  for f in "$root"/scrum/design-*/DesignBacklog.md; do
    [ -f "$f" ] || continue
    n_designs=$((n_designs + 1))
    design_file=$f
  done

  nl='
'
  case $key in
    承诺)
      head_line='本项目日志里的承诺（原文）：'
      colon='：' open='（' close='）'
      many_sprints='有 %s 个冲刺开着，见看板'
      many_designs='有 %s 个设计开着，见看板'
      design_label='设计目标'
      ;;
    *)
      head_line="Commitments from this project's logs (verbatim):"
      colon=': ' open=' (' close=')'
      many_sprints='%s Sprints are open; see the board'
      many_designs='%s designs are open; see the board'
      design_label='Design goal'
      ;;
  esac

  out=$head_line
  [ -n "$product" ] && out=$out${nl}Product$colon$product
  [ -n "$goal" ] && out=$out${nl}Product\ Goal$colon$goal
  if [ "$n_sprints" -eq 1 ]; then
    text=$(clean "$(field "$(read_commitments "$sprint_file")" sprint 3)") &&
      out=$out${nl}Sprint\ Goal$open$(basename "$(dirname "$sprint_file")")$close$colon$text
  elif [ "$n_sprints" -gt 1 ]; then
    out=$out$nl$(printf "$many_sprints" "$n_sprints")
  fi
  if [ "$n_designs" -eq 1 ]; then
    text=$(clean "$(field "$(read_commitments "$design_file")" design 3)") &&
      out=$out$nl$design_label$open$(basename "$(dirname "$design_file")")$close$colon$text
  elif [ "$n_designs" -gt 1 ]; then
    out=$out$nl$(printf "$many_designs" "$n_designs")
  fi

  # TEST-ONLY (Sprint 19 frequency test): the way UserPromptSubmit decides whether to inject. SessionStart
  # always injects. Remove this block, and the state it keeps, once the frequency is chosen.
  mode=${IDEO_SCRUM_COMMITMENTS_MODE:-start}
  n=${IDEO_SCRUM_COMMITMENTS_N:-5}
  case $n in '' | *[!0-9]* | 0) n=5 ;; esac
  state_dir=${CLAUDE_PLUGIN_DATA:-${TMPDIR:-/tmp}}/ideo-scrum-commitments
  mkdir -p "$state_dir" 2>/dev/null
  state=$state_dir/${session:-nosession}
  fp=$(printf '%s' "$out" | cksum | awk '{ print $1 "-" $2 }')
  inject=0
  case $event in
    SessionStart)
      inject=1
      printf '%s' "$fp" > "$state.fp" 2>/dev/null
      [ "$source" = startup ] && printf '0' > "$state.count" 2>/dev/null
      ;;
    UserPromptSubmit)
      case $mode in
        every) inject=1 ;;
        every-n)
          c=$(cat "$state.count" 2>/dev/null)
          c=$((${c:-0} + 1))
          printf '%s' "$c" > "$state.count" 2>/dev/null
          [ $((c % n)) -eq 0 ] && inject=1
          ;;
        changed)
          old=$(cat "$state.fp" 2>/dev/null)
          if [ "$fp" != "$old" ]; then
            inject=1
            printf '%s' "$fp" > "$state.fp" 2>/dev/null
          fi
          ;;
      esac
      ;;
  esac
  [ "$inject" -eq 1 ] && printf '%s\n' "$out"
  return 0
}

main 2>/dev/null
exit 0
