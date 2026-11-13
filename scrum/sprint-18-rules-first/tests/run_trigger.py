"""运行本冲刺已冻结的触发对照；原始输出仅写仓库外临时目录。"""

import argparse
import concurrent.futures
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from pathlib import Path

TESTS = Path(__file__).resolve().parent
ROOT = TESTS.parents[2]
DATA = json.loads((TESTS / "cases.json").read_text(encoding="utf-8"))
MODEL_LABEL = "magpie 的便宜模型，非 Haiku"


def local_day():
    return subprocess.check_output(
        ["powershell.exe", "-NoProfile", "-Command", "Get-Date -Format 'yyyy-MM-dd'"],
        text=True,
    ).strip()


def records(text):
    output = []
    for line in text.splitlines():
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            output.append(value)
        elif isinstance(value, list):
            output.extend(item for item in value if isinstance(item, dict))
    return output


def parse(text):
    events = records(text)
    calls = {}
    failed = set()
    readable = set()
    answer = ""
    denied = []
    subtype = None
    api_error = False
    for event in events:
        if event.get("parent_tool_use_id"):
            continue
        event_type = event.get("type")
        message = event.get("message", {})
        for block in message.get("content", []) if isinstance(message, dict) else []:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                calls[block.get("id")] = block
            elif block.get("type") == "tool_result":
                use_id = block.get("tool_use_id")
                if block.get("is_error"):
                    failed.add(use_id)
                else:
                    content = block.get("content", "")
                    if isinstance(content, list):
                        content = "\n".join(part.get("text", "") for part in content if isinstance(part, dict))
                    if str(content).strip():
                        readable.add(use_id)
        if event_type == "result":
            answer = event.get("result", "")
            subtype = event.get("subtype")
            denied = event.get("permission_denials", [])
            api_error = bool(event.get("is_error"))
    skills = []
    read_calls = []
    for use_id, call in calls.items():
        if use_id in failed:
            continue
        params = call.get("input", {})
        if call.get("name") == "Skill":
            skill = params.get("skill", "").removeprefix("ideo-scrum:")
            if skill:
                skills.append(skill)
        if call.get("name") in ("Read", "Grep") and use_id in readable:
            if call["name"] == "Grep" and params.get("output_mode", "files_with_matches") != "content":
                continue
            path = params.get("file_path", params.get("path", ""))
            read_calls.append({"tool": call["name"], "path": path.replace("\\", "/"), "pattern": params.get("pattern")})
    return {"skills": sorted(set(skills)), "read_calls": read_calls, "answer": answer, "subtype": subtype, "api_error": api_error, "denials": len(denied)}


def grade(case, result):
    skills = set(result["skills"])
    forbidden = sorted(skills & set(DATA["restricted_kernels"]))
    trigger = not forbidden if case["group"] == "A" else set(case["target_skills"]).issubset(skills)
    reads = {}
    for expected in case["required_reads"]:
        reads[expected] = any(re.search(expected.replace(".", r"\."), call["path"]) for call in result["read_calls"])
    return {"trigger_ok": trigger, "forbidden_kernels": forbidden, "required_reads": reads}


def self_test():
    success = "\n".join(json.dumps(event) for event in [
        {"type": "assistant", "message": {"content": [
            {"type": "tool_use", "id": "s", "name": "Skill", "input": {"skill": "ideo-scrum:scrum-kernel"}},
            {"type": "tool_use", "id": "r", "name": "Read", "input": {"file_path": "C:/plugin/scrum-kernel/conventions/product-log.md"}},
            {"type": "tool_use", "id": "g", "name": "Grep", "input": {"path": "C:/plugin/sprint-kernel/conventions/sprint-log.md", "output_mode": "files_with_matches"}},
        ]}},
        {"type": "user", "message": {"content": [
            {"type": "tool_result", "tool_use_id": "s", "content": "Loaded"},
            {"type": "tool_result", "tool_use_id": "r", "content": "1 Product log"},
            {"type": "tool_result", "tool_use_id": "g", "content": "filename only"},
        ]}},
        {"type": "result", "subtype": "success", "result": "Done", "permission_denials": []},
    ])
    actual = parse(success)
    assert actual["skills"] == ["scrum-kernel"]
    assert len(actual["read_calls"]) == 1
    assert grade(DATA["cases"][5], actual)["trigger_ok"]
    assert not grade(DATA["cases"][0], actual)["trigger_ok"]
    assert parse('{"type":"result","subtype":"success","result":"scrum-kernel"}')["skills"] == []
    denied = success + '\n{"type":"user","message":{"content":[{"type":"tool_result","tool_use_id":"s","is_error":true,"content":"denied"}]}}'
    assert parse(denied)["skills"] == []
    print("触发判定自测：通过（成功调用、漏触发、仅文字、只列文件名、调用失败）", flush=True)


def environment(temp):
    # 两个冲刺共用的最小白名单；不继承宿主模型、认证、目录或消息通道。
    allowed = ("SystemRoot", "PATH", "USERPROFILE", "APPDATA", "LOCALAPPDATA", "HOMEDRIVE", "HOMEPATH", "ComSpec", "PATHEXT", "TEMP", "TMP")
    parent = {key.casefold(): value for key, value in os.environ.items()}
    env = {key: parent[key.casefold()] for key in allowed if key.casefold() in parent}
    env.update({"CLAUDE_CODE_GIT_BASH_PATH": r"E:\GIT\Git\usr\bin\bash.exe", "TEMP": str(temp), "TMP": str(temp), "MSYS_NO_PATHCONV": "1"})
    return env


def stop_process_tree(process):
    # cmd 的退出不代表其下的 CLI 已退出；先杀整棵树，再回收直接子进程。
    if os.name == "nt":
        killed = subprocess.run(["taskkill.exe", "/PID", str(process.pid), "/T", "/F"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20)
        if killed.returncode != 0 and process.poll() is None:
            process.kill()
        process.wait(timeout=20)
        return killed.returncode
    process.kill()
    process.wait(timeout=20)
    return 0


def invoke(folder, plugin, prompt, timeout=300):
    cwd = folder / "work"
    temp = folder / "temp"
    cwd.mkdir(parents=True, exist_ok=True)
    temp.mkdir(parents=True, exist_ok=True)
    wrapper = shutil.which("claude-magpie.cmd")
    if not wrapper:
        raise RuntimeError("缺少 claude-magpie.cmd")
    args = [wrapper, "-p", "--model", "haiku", "--plugin-dir", str(plugin), "--add-dir", str(plugin),
            "--tools", "Read,Grep,Glob,Skill", "--allowedTools", "Read,Grep,Glob,Skill",
            "--disallowedTools", "Bash,PowerShell,Write,Edit,Agent", "--permission-prompts", "none",
            "--setting-sources", "user", "--settings", '{"disableAllHooks":true}',
            "--strict-mcp-config", "--no-session-persistence", "--output-format", "stream-json", "--verbose"]
    timed_out = False
    tree_kill_code = None
    with (folder / "raw.jsonl").open("w", encoding="utf-8") as out, (folder / "stderr.txt").open("w", encoding="utf-8") as err:
        process = subprocess.Popen(args, stdin=subprocess.PIPE, text=True, encoding="utf-8", cwd=cwd, env=environment(temp), stdout=out, stderr=err)
        try:
            process.communicate(input=prompt, timeout=timeout)
            code = process.returncode
        except subprocess.TimeoutExpired:
            timed_out = True
            tree_kill_code = stop_process_tree(process)
            code = -1
    result = parse((folder / "raw.jsonl").read_text(encoding="utf-8", errors="replace"))
    result["exit_code"] = code
    result["timeout_seconds"] = timeout
    result["timed_out"] = timed_out
    result["tree_kill_exit_code"] = tree_kill_code
    result["technical_error"] = code != 0 or result["subtype"] != "success" or result["api_error"]
    return result


def prepare():
    run = Path(tempfile.mkdtemp(prefix="ideo-s18-trigger-"))
    ref = subprocess.check_output(["git", "rev-parse", "refs/heads/main"], cwd=ROOT, text=True).strip()
    archive = subprocess.check_output(["git", "archive", "--format=zip", ref, "plugins/ideo-scrum"], cwd=ROOT)
    source = run / "baseline-source"
    source.mkdir()
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        for member in zipped.infolist():
            target = (source / member.filename).resolve()
            if not target.is_relative_to(source.resolve()):
                raise RuntimeError("基线快照路径越界")
        zipped.extractall(source)
    (run / "run.json").write_text(json.dumps({"baseline": ref, "prepared_day": local_day(), "model_label": MODEL_LABEL}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(str(run), flush=True)
    print(f"baseline={ref}", flush=True)


def smoke(run, name):
    folder = run / name
    work = folder / "work"
    work.mkdir(parents=True)
    (work / "probe.txt").write_text("读取正常", encoding="utf-8")
    result = invoke(folder, ROOT / "plugins/ideo-scrum", "读取当前目录 probe.txt，只回复文件内容。")
    status = not result["technical_error"] and any(call["path"].endswith("probe.txt") for call in result["read_calls"]) and "读取正常" in result["answer"]
    (folder / "parsed.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"冒烟：{'PASS' if status else 'FAIL'}；工具读取={'是' if result['read_calls'] else '否'}；技术错误={'是' if result['technical_error'] else '否'}；{MODEL_LABEL}", flush=True)
    if not status:
        raise SystemExit(1)


def suite(run, name, workers, only=None, timeout=300, stop_at_midnight=False):
    group_folder = run / name
    if group_folder.exists():
        raise RuntimeError("该组已有输出，请用新的组名保留旧记录")
    group_folder.mkdir()
    plugin = run / "baseline-source/plugins/ideo-scrum" if name.startswith("baseline") else ROOT / "plugins/ideo-scrum"
    selected = [case for case in DATA["cases"] if not only or case["id"] in only]
    if only and set(only) != {case["id"] for case in selected}:
        raise RuntimeError("补跑题号不在冻结题目内")
    tasks = [(case, number) for case in selected for number in range(1, DATA["repetitions"] + 1)]
    results = []
    start_day = local_day()
    deadline = None
    if stop_at_midnight:
        seconds = float(subprocess.check_output(["powershell.exe", "-NoProfile", "-Command", "[Math]::Floor(((Get-Date).Date.AddDays(1) - (Get-Date)).TotalSeconds)"], text=True).strip())
        deadline = time.monotonic() + max(0, seconds - 1)

    def work(task):
        case, number = task
        folder = group_folder / f"{case['id']}-r{number}"
        cwd = folder / "work"
        cwd.mkdir(parents=True)
        for relative in case["fixture_files"]:
            target = cwd / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(TESTS / "fixtures/project" / relative, target)
        remaining = timeout if deadline is None else min(timeout, deadline - time.monotonic())
        if remaining <= 0:
            result = {"skills": [], "read_calls": [], "answer": "", "subtype": None, "api_error": False, "denials": 0, "exit_code": -2, "technical_error": True, "midnight_cutoff": True}
        else:
            result = invoke(folder, plugin, case["prompt"], timeout=remaining)
        result.update({"case": case["id"], "group": case["group"], "repeat": number, "grade": grade(case, result)})
        (folder / "parsed.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for result in pool.map(work, tasks):
            results.append(result)
            print(f"{name} {result['case']}-r{result['repeat']}: {'ERROR' if result['technical_error'] else '完成'}；目标触发={'是' if result['grade']['trigger_ok'] else '否'}；拒读={result['denials']}", flush=True)
    summary = {"suite": name, "model_label": MODEL_LABEL, "start_day": start_day, "end_day": local_day(), "selected_cases": [case["id"] for case in selected], "timeout_seconds": timeout, "stop_at_midnight": stop_at_midnight, "results": results}
    (group_folder / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    errors = sum(result["technical_error"] for result in results)
    print(f"{name}: {len(results)} 次，技术错误 {errors}；原始记录仅在仓库外。", flush=True)
    if errors:
        raise SystemExit(1)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--run-dir", type=Path)
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--smoke-name", default="smoke")
    parser.add_argument("--suite")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--cases", nargs="+")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--stop-at-midnight", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.prepare:
        prepare()
    elif args.smoke:
        smoke(args.run_dir, args.smoke_name)
    elif args.suite:
        suite(args.run_dir, args.suite, args.workers, args.cases, args.timeout, args.stop_at_midnight)
    else:
        parser.error("请选择准备、自测、冒烟或一组测试")


if __name__ == "__main__":
    main()
