#!/bin/sh
# IDEO-Scrum: put the commitments written in this project's logs into Claude's context.
#
# Same behaviour as the Sprint 19 hook, with the per-prompt external processes removed: one awk pass
# over the logs, POSIX shell for everything else.
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
# POSIX sh; the only external program on the normal path is awk (plus mkdir the first time the state
# folder is created, and the prune pipeline on a startup once the folder holds more than 200 files).

[ "$IDEO_SCRUM_COMMITMENTS" = "off" ] && exit 0

# Copy $1 into __path with every backslash turned into a slash.
to_slashes() {
  __path=$1
  while :; do
    case $__path in
      *\\*) __path=${__path%%\\*}/${__path#*\\} ;;
      *) break ;;
    esac
  done
}

# Walk up from $1 until a directory holds scrum/ProductBacklog.md; put it in __root.
find_root_set() {
  to_slashes "$1"
  d=$__path
  i=0
  while [ -n "$d" ] && [ "$i" -lt 64 ]; do
    if [ -f "$d/scrum/ProductBacklog.md" ]; then
      __root=$d
      return 0
    fi
    case $d in
      [A-Za-z]:) return 1 ;;
      */*) p=${d%/*}; [ -n "$p" ] || p=/ ;;
      *) p=. ;;
    esac
    [ "$p" = "$d" ] && return 1
    d=$p
    i=$((i + 1))
  done
  return 1
}

# Skip the whitespace in front of $v (space, tab, CR, LF); JSON allows it around the colon.
strip_blanks() {
  while :; do
    case $v in
      [[:space:]]*) v=${v#?} ;;
      *) break ;;
    esac
  done
}

# Take the string value of the JSON key $2 out of the text $1; put it in __value.
json_field() {
  case $1 in
    *\"$2\"*) ;;
    *) __value=; return 1 ;;
  esac
  v=${1#*\"$2\"}
  strip_blanks
  case $v in
    :*) v=${v#:} ;;
    *) __value=; return 1 ;;
  esac
  strip_blanks
  case $v in
    \"*) v=${v#\"} ;;
    *) __value=; return 1 ;;
  esac
  __value=${v%%\"*}
  return 0
}

# Keep the 200 newest state files of the folder $1 and remove the rest, so that it does not grow for ever.
prune() {
  __prune_dir=$1
  set -- "$__prune_dir"/*.fp
  [ -e "$1" ] || return 0
  [ "$#" -le 200 ] && return 0
  ls -t "$__prune_dir" 2>/dev/null | grep '\.fp$' | tail -n +201 | while read -r f; do rm -f "$__prune_dir/$f"; done
}

main() {
  input=
  while IFS= read -r line || [ -n "$line" ]; do
    input=$input$line
  done <&0
  meta=${input%%\"prompt\"*}

  event=
  json_field "$meta" hook_event_name && case $__value in
    *[!A-Za-z]*) ;;
    *) event=$__value ;;
  esac
  session=
  json_field "$meta" session_id && case $__value in
    *[!A-Za-z0-9_-]*) ;;
    *) session=$__value ;;
  esac
  source=
  json_field "$meta" source && case $__value in
    *[!a-z]*) ;;
    *) source=$__value ;;
  esac
  case $event in
    SessionStart | UserPromptSubmit) ;;
    *) return 0 ;;
  esac

  if find_root_set "$PWD"; then
    root=$__root
  elif find_root_set "$CLAUDE_PROJECT_DIR"; then
    root=$__root
  else
    return 0
  fi

  prod_file=$root/scrum/ProductBacklog.md
  [ -r "$prod_file" ] || return 0

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

  set -- "$prod_file"
  if [ "$n_sprints" -eq 1 ] && [ -r "$sprint_file" ]; then set -- "$@" "$sprint_file"; fi
  if [ "$n_designs" -eq 1 ] && [ -r "$design_file" ]; then set -- "$@" "$design_file"; fi

  # One pass over the logs: strip CRs, follow the headings, take the first row of each kind.
  res=$(awk '
    FILENAME != last { last = FILENAME; heading = "" }
    {
      gsub(/\r/, "")
      if ($0 ~ /^#/) { heading = $0; next }
      if ($0 ~ /^\|[ \t]*(承诺|Commitment)[ \t]*\|/) {
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
        if (kind != "") {
          cur = "prod"
          if (FILENAME ~ /SprintBacklog\.md$/) cur = "sprint"
          else if (FILENAME ~ /DesignBacklog\.md$/) cur = "design"
          k = cur SUBSEP kind
          if (!(k in seen)) {
            seen[k] = 1
            printf "%s\t%s\t%s\t%s\n", cur, kind, key, text
          }
        }
      }
    }' "$@")

  product_text= goal_text= product_key= goal_key= sprint_text= design_text=
  while IFS='	' read -r cur kind key text rest; do
    case $cur.$kind in
      prod.product) product_text=$text; product_key=$key ;;
      prod.productgoal) goal_text=$text; goal_key=$key ;;
      sprint.sprint) sprint_text=$text ;;
      design.design) design_text=$text ;;
    esac
  done <<EOF
$res
EOF

  # Print the text unless it is empty or an unfilled template placeholder such as <Sprint Goal>.
  product=
  case $product_text in
    '' | '<'*'>') ;;
    *) product=$product_text ;;
  esac
  goal=
  case $goal_text in
    '' | '<'*'>') ;;
    *) goal=$goal_text ;;
  esac
  [ -n "$product$goal" ] || return 0
  key=$product_key
  [ -n "$key" ] || key=$goal_key

  nl='
'
  case $key in
    承诺)
      head_line='本项目日志里的承诺（原文）：'
      colon='：' open='（' close='）'
      many_sprints_pre='有 ' many_sprints_post=' 个冲刺开着，见看板'
      many_designs_pre='有 ' many_designs_post=' 个设计开着，见看板'
      design_label='设计目标'
      ;;
    *)
      head_line="Commitments from this project's logs (verbatim):"
      colon=': ' open=' (' close=')'
      many_sprints_pre='' many_sprints_post=' Sprints are open; see the board'
      many_designs_pre='' many_designs_post=' designs are open; see the board'
      design_label='Design goal'
      ;;
  esac

  out=$head_line
  [ -n "$product" ] && out=$out${nl}Product$colon$product
  [ -n "$goal" ] && out=$out${nl}Product\ Goal$colon$goal
  if [ "$n_sprints" -eq 1 ]; then
    case $sprint_text in
      '' | '<'*'>') ;;
      *)
        __dir=${sprint_file%/*}
        out=$out${nl}Sprint\ Goal$open${__dir##*/}$close$colon$sprint_text
        ;;
    esac
  elif [ "$n_sprints" -gt 1 ]; then
    out=$out$nl$many_sprints_pre$n_sprints$many_sprints_post
  fi
  if [ "$n_designs" -eq 1 ]; then
    case $design_text in
      '' | '<'*'>') ;;
      *)
        __dir=${design_file%/*}
        out=$out$nl$design_label$open${__dir##*/}$close$colon$design_text
        ;;
    esac
  elif [ "$n_designs" -gt 1 ]; then
    out=$out$nl$many_designs_pre$n_designs$many_designs_post
  fi

  # When to inject. SessionStart always does (a new session, a resume, a clear, a compaction: the context has
  # lost the text, or never had it). UserPromptSubmit does only when the commitments differ from what was last
  # injected in this session, so a goal changed outside the conversation reaches Claude, and an unchanged one
  # costs nothing after the first injection. The last injected text is kept in a file named by the session,
  # in the plugin's data folder; if that cannot be written, the text is injected again (it is only a few
  # lines). Sprint 19's frequency test chose this over injecting on every prompt or every few prompts.
  # The stored text is the commitments themselves, not a checksum: the comparison cannot collide, and it
  # still reads the logs on every prompt (no file size or mtime shortcut).
  state_dir=${CLAUDE_PLUGIN_DATA:-${TMPDIR:-/tmp}}/ideo-scrum-commitments
  [ -d "$state_dir" ] || mkdir -p "$state_dir" 2>/dev/null
  state=$state_dir/${session:-nosession}.fp
  inject=0
  case $event in
    SessionStart)
      inject=1
      printf '%s' "$out" > "$state" 2>/dev/null
      [ "$source" = startup ] && prune "$state_dir"
      ;;
    UserPromptSubmit)
      old=
      first=1
      if [ -r "$state" ]; then
        while IFS= read -r line || [ -n "$line" ]; do
          if [ "$first" = 1 ]; then old=$line; first=0; else old=$old$nl$line; fi
        done < "$state"
      fi
      if [ "$out" != "$old" ]; then
        inject=1
        printf '%s' "$out" > "$state" 2>/dev/null
      fi
      ;;
  esac
  [ "$inject" -eq 1 ] && printf '%s\n' "$out"
  return 0
}

main 2>/dev/null
exit 0
