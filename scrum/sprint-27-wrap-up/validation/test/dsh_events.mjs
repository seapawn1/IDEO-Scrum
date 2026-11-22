// Sprint 27 Test, item 3 (DSH installed acceptance): read the native events of one DSH session and check what the
// acceptance asked for. The evidence is the event record, not what the model said afterwards. Read-only.
//
//   node dsh_events.mjs SESSION.session.v4.jsonl.zstd           the checks for the /supporter acceptance (the Test session)
//   node dsh_events.mjs --reads SESSION.session.v4.jsonl.zstd   only the facts and the read calls (the earlier probe)
//   node dsh_events.mjs --selftest
//
// The record is data from a model run: it is decompressed and parsed as JSON, never run. Needs a Node whose zlib has
// zstdDecompressSync (Node 22.15 or later).
import fs from "node:fs";
import zlib from "node:zlib";

const TEMPLATE_PATH = /\/skills\/scrum-kernel\/\.\.\/\.\.\/template\/sprint-backlog-template\.md$/;

/** The file policy and the approval policy in force when the first turn started. */
function policyAtFirstTurn(events) {
  let preset, approval;
  for (const e of events) {
    if (e.type === "turn/start") break;
    if (e.type === "permission/preset") preset = e.data?.preset;
    if (e.type === "approval/policy") approval = e.data?.policy;
  }
  return { preset, approval };
}

/** The read calls of a session and what became of each (the earlier probe read package files from outside its workspace). */
export function reads(events) {
  const results = events.filter((e) => e.type === "tool/result");
  return events.filter((e) => e.type === "tool/call" && e.data?.name === "read").map((call) => {
    const result = results.find((r) => (r.sourceEventSeqs ?? []).includes(call.seq));
    let args = {};
    try { args = JSON.parse(call.data.arguments ?? "{}"); } catch { /* an unreadable argument string stays empty */ }
    return { call: call.seq, result: result?.seq, path: args.file_path, isError: result?.data?.message?.isError,
             resolved: result?.data?.meta?.path, lines: result?.data?.meta?.lines?.length, total: result?.data?.meta?.totalLines };
  });
}

/** All checks over the events of one session. Returns { checks: [{ name, ok, detail }], facts: [string] }. */
export function check(events) {
  const checks = [];
  const add = (name, ok, detail = "") => checks.push({ name, ok: Boolean(ok), detail });
  const of = (type) => events.filter((e) => e.type === type);
  const text = (e) => (e.data?.content ?? []).map((b) => b?.text ?? "").join("");

  // 1. /supporter was recognised and expanded into the role's own instructions
  const invocation = of("user/message").find((e) => e.data?.source?.kind === "skill-invocation" && e.data?.source?.name === "supporter");
  const body = invocation ? text(invocation) : "";
  add('1. /supporter is expanded: a user/message from source skill-invocation, name supporter, opening <skill_content name="supporter">',
      invocation && body.startsWith('<skill_content name="supporter">'), invocation ? `seq ${invocation.seq}` : "no such event");

  // 2. the kernels preloaded in that same event are ideo-kernel, then scrum-kernel, and no other
  const preloaded = [...body.matchAll(/Preloaded kernel: ([a-z-]+)/g)].map((m) => m[1]);
  add("2. preloaded in that event: ideo-kernel, then scrum-kernel, and no other (no sprint-kernel, no design-kernel)",
      JSON.stringify(preloaded) === JSON.stringify(["ideo-kernel", "scrum-kernel"]), preloaded.join(" -> ") || "none");

  // 3. the template at its new place is read through ../../template/ from the scrum-kernel folder, without error
  const calls = of("tool/call");
  const argsOf = (e) => { try { return JSON.parse(e.data?.arguments ?? "{}"); } catch { return {}; } };
  const read = calls.find((e) => e.data?.name === "read" && TEMPLATE_PATH.test(argsOf(e).file_path ?? ""));
  const result = read && of("tool/result").find((e) => (e.sourceEventSeqs ?? []).includes(read.seq));
  const lines = result?.data?.meta?.lines ?? [];
  add("3. a read call used .../skills/scrum-kernel/../../template/sprint-backlog-template.md and its result is not an error",
      read && result && result.data?.message?.isError === false && lines.length > 0,
      read ? `call seq ${read.seq}, result seq ${result?.seq}, isError ${result?.data?.message?.isError}, lines ${lines.length} of ${result?.data?.meta?.totalLines}` : "no such call");
  add("3b. the file that was read is plugins/ideo-scrum/template/sprint-backlog-template.md",
      /plugins[\\/]ideo-scrum[\\/]template[\\/]sprint-backlog-template\.md$/.test(result?.data?.meta?.path ?? ""), result?.data?.meta?.path ?? "no path");

  // the session did nothing else: one tool call, and no command but the permission switch
  const commands = of("command/run").map((e) => e.data?.name);
  add("4. the whole session made exactly one tool call (read) and ran no command but /permission",
      calls.length === 1 && calls[0].data?.name === "read" && commands.every((c) => c === "permission"),
      `tool calls: ${calls.map((e) => e.data?.name).join(", ") || "none"}; commands: ${commands.join(", ") || "none"}`);

  const { preset, approval } = policyAtFirstTurn(events);
  add("5. at the first turn the permission preset is workspace-write and the approval policy is ask", preset === "workspace-write" && approval === "ask",
      `preset ${preset}, approval ${approval}`);

  const facts = [];
  const header = events.find((e) => e.type === "session");
  const context = of("request/context")[0];
  const base = /Base directory for this skill: ([^\n]+)/.exec(body)?.[1];
  facts.push(`session ${header?.id}; cwd ${header?.cwd}; agent preset ${of("agent-preset/selected")[0]?.data?.agentPreset}`);
  facts.push(`model ${context?.data?.model} (provider ${context?.data?.provider}); ${events.length} events`);
  facts.push(`skill base directory: ${base}`);
  return { checks, facts };
}

/** A small synthetic session in the shape of the real record; the self-test breaks one thing at a time. */
function synthetic(mutate = {}) {
  const preloads = mutate.preloads ?? ["ideo-kernel", "scrum-kernel"];
  const events = [
    { type: "session", id: "synthetic", cwd: "S:\\IDEO-Scrum" },
    { type: "permission/preset", seq: 0, data: { preset: mutate.preset ?? "workspace-write" } },
    { type: "approval/policy", seq: 1, data: { policy: "ask" } },
    { type: "agent-preset/selected", seq: 2, data: { agentPreset: "standard" } },
    { type: "turn/start", seq: 3, data: {} },
    { type: "user/message", seq: 4, data: { source: { kind: "skill-invocation", name: "supporter" },
      content: [{ type: "text", text: '<skill_content name="supporter">\nBase directory for this skill: S:\\x\n' + preloads.map((k) => `Preloaded kernel: ${k}\n`).join("") }] } },
    { type: "request/context", seq: 5, data: { provider: "p", model: "m" } },
    { type: "tool/call", seq: 6, data: { name: "read", arguments: JSON.stringify({ file_path: "S:/x/plugins/ideo-scrum/skills/scrum-kernel/../../template/sprint-backlog-template.md" }) } },
    { type: "tool/result", seq: 7, sourceEventSeqs: [6], data: { message: { isError: mutate.isError ?? false },
      meta: { path: "S:\\x\\plugins\\ideo-scrum\\template\\sprint-backlog-template.md", lines: [{ number: 1, text: "#" }], totalLines: 54 } } },
  ];
  if (mutate.extraCall) events.push({ type: "tool/call", seq: 8, data: { name: "bash", arguments: "{}" } });
  return events;
}

function selftest() {
  const failing = (events) => check(events).checks.filter((c) => !c.ok).map((c) => c.name.split(".")[0]);
  const cases = [
    ["a good session passes everything", synthetic(), []],
    ["kernels in the wrong order fail check 2", synthetic({ preloads: ["scrum-kernel", "ideo-kernel"] }), ["2"]],
    ["an extra preloaded kernel fails check 2", synthetic({ preloads: ["ideo-kernel", "scrum-kernel", "sprint-kernel"] }), ["2"]],
    ["a read that ends in error fails check 3", synthetic({ isError: true }), ["3"]],
    ["a second tool call fails check 4 (one tool call only)", synthetic({ extraCall: true }), ["4"]],
    ["a full-access preset fails check 5 (policy at the first turn)", synthetic({ preset: "danger-full-access" }), ["5"]],
  ];
  let bad = 0;
  for (const [name, events, expected] of cases) {
    const got = failing(events);
    const ok = JSON.stringify(got) === JSON.stringify(expected);
    bad += ok ? 0 : 1;
    console.log(`${ok ? "PASS" : "FAIL"} selftest: ${name}${ok ? "" : ` (failed ${JSON.stringify(got)}, expected ${JSON.stringify(expected)})`}`);
  }
  // --reads: one row per read call, carrying the result's error flag, resolved path and line counts
  for (const [name, events, isError] of [["--reads reports a good read", synthetic(), false], ["--reads reports a read that ends in error", synthetic({ isError: true }), true]]) {
    const rows = reads(events);
    const ok = rows.length === 1 && rows[0].isError === isError && rows[0].call === 6 && rows[0].result === 7 && rows[0].lines === 1 && rows[0].total === 54;
    bad += ok ? 0 : 1;
    console.log(`${ok ? "PASS" : "FAIL"} selftest: ${name}${ok ? "" : ` (got ${JSON.stringify(rows)})`}`);
  }
  return bad ? 1 : 0;
}

function loadEvents(file) {
  const raw = zlib.zstdDecompressSync(fs.readFileSync(file)).toString("utf8");
  return raw.split("\n").filter((l) => l.trim()).map((l) => JSON.parse(l));
}

/** --reads: no verdict, only what the record says about where the session worked and what its reads returned. */
function printReads(events) {
  const header = events.find((e) => e.type === "session");
  const { preset, approval } = policyAtFirstTurn(events);
  const approvalRequests = events.filter((e) => /^approval\//.test(e.type) && e.type !== "approval/policy").length;
  console.log(`fact: session ${header?.id}; cwd ${header?.cwd}; preset ${preset}, approval ${approval} at the first turn`);
  console.log(`fact: model ${events.find((e) => e.type === "request/context")?.data?.model}; ${events.length} events; approval request events: ${approvalRequests}`);
  console.log(`fact: tool calls: ${events.filter((e) => e.type === "tool/call").map((e) => e.data?.name).join(", ") || "none"}`);
  for (const r of reads(events)) {
    console.log(`read: call seq ${r.call}, result seq ${r.result}: ${r.path} -> isError ${r.isError}, resolved ${r.resolved}, ${r.lines} of ${r.total} lines`);
  }
  return 0;
}

function main() {
  const [arg, file] = process.argv.slice(2);
  if (arg === "--selftest") return selftest();
  if (arg === "--reads" && file) return printReads(loadEvents(file));
  if (!arg) { console.error("usage: node dsh_events.mjs SESSION.jsonl.zstd | --reads SESSION.jsonl.zstd | --selftest"); return 2; }
  const events = loadEvents(arg);
  const { checks, facts } = check(events);
  for (const c of checks) console.log(`${c.ok ? "PASS" : "FAIL"} ${c.name}${c.detail ? " -- " + c.detail : ""}`);
  for (const f of facts) console.log(`fact: ${f}`);
  const failed = checks.filter((c) => !c.ok).length;
  console.log(failed ? `\n${failed} check(s) failed` : "\nall checks passed");
  return failed ? 1 : 0;
}

process.exitCode = main();
