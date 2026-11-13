"""只汇总触发事实；内容由 Developer 逐条看答案，不调用另一个模型判分。"""

import argparse
import json
import sys
from pathlib import Path


def load(run, suite):
    return json.loads((run / suite / "summary.json").read_text(encoding="utf-8"))


def compact(data):
    rows = []
    results = data["results"]
    for case in sorted({item["case"] for item in results}):
        trials = [item for item in results if item["case"] == case]
        rows.append({
            "case": case,
            "trigger_ok": sum(item["grade"]["trigger_ok"] for item in trials),
            "runs": len(trials),
            "technical_errors": sum(item["technical_error"] for item in trials),
            "required_reads_all": sum(all(item["grade"]["required_reads"].values()) for item in trials),
            "skills_by_trial": {str(item["repeat"]): item["skills"] for item in trials},
            "missed_reads": {str(item["repeat"]): [key for key, yes in item["grade"]["required_reads"].items() if not yes] for item in trials},
        })
    groups = {}
    for group in ("A", "B", "C", "D"):
        trials = [item for item in results if item["group"] == group]
        groups[group] = {
            "runs": len(trials),
            "trigger_ok": sum(item["grade"]["trigger_ok"] for item in trials),
            "technical_errors": sum(item["technical_error"] for item in trials),
        }
    groups["A"]["misfire_trials"] = groups["A"]["runs"] - groups["A"]["trigger_ok"]
    return {"suite": data["suite"], "model_label": data["model_label"], "start_day": data["start_day"], "end_day": data["end_day"], "cases": rows, "groups": groups}


def compare(baseline, revised):
    old = compact(baseline)
    new = compact(revised)
    rows = {row["case"]: row for row in new["cases"]}
    old_rows = {row["case"]: row for row in old["cases"]}
    gates = {
        "A": new["groups"]["A"]["misfire_trials"] <= 1,
        "B": new["groups"]["B"]["trigger_ok"] >= 8,
        "C": new["groups"]["C"]["trigger_ok"] >= 7 and new["groups"]["C"]["trigger_ok"] >= old["groups"]["C"]["trigger_ok"],
        "D1": rows["D1"]["trigger_ok"] >= old_rows["D1"]["trigger_ok"],
        "D2": rows["D2"]["trigger_ok"] >= old_rows["D2"]["trigger_ok"],
    }
    complete = len(baseline["results"]) == len(revised["results"]) == 33 and not any(item["technical_error"] for item in baseline["results"] + revised["results"])
    days = {old["start_day"], old["end_day"], new["start_day"], new["end_day"]}
    valid = complete and len(days) == 1 and old["model_label"] == new["model_label"]
    print("模型标注：" + new["model_label"])
    print(f"有效对照：{valid}；33次齐全无技术错：{complete}；同日：{len(days) == 1}")
    print("| 题 | 基线触发符合 | 新版触发符合 | 基线必读全读 | 新版必读全读 |")
    print("| --- | --- | --- | --- | --- |")
    for case in sorted(rows):
        a, b = old_rows[case], rows[case]
        reads_a = "—" if case.startswith("A") else str(a["required_reads_all"]) + "/3"
        reads_b = "—" if case.startswith("A") else str(b["required_reads_all"]) + "/3"
        print(f"| {case} | {a['trigger_ok']}/3 | {b['trigger_ok']}/3 | {reads_a} | {reads_b} |")
    print("A行的符合表示未误触发，不是内核加载次数。")
    print("冻结门槛：" + json.dumps(gates, ensure_ascii=False))
    print("整体行为过线：" + str(valid and all(gates.values())))
    print("内容仍须逐条核对，不能抵行为。")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--suites", nargs="+", default=["baseline", "revised"])
    parser.add_argument("--answers", nargs="*")
    parser.add_argument("--compare", action="store_true")
    args = parser.parse_args()
    if args.compare:
        if len(args.suites) != 2:
            parser.error("比较必须给出基线与新版两组")
        compare(load(args.run_dir, args.suites[0]), load(args.run_dir, args.suites[1]))
        return
    for suite in args.suites:
        data = load(args.run_dir, suite)
        if args.answers is not None:
            for result in data["results"]:
                if not args.answers or result["case"] in args.answers:
                    print(f"\n=== {suite} {result['case']}-r{result['repeat']} ===")
                    print("skills=" + ",".join(result["skills"]))
                    print("reads=" + json.dumps(result["grade"]["required_reads"], ensure_ascii=False))
                    print(result["answer"])
        else:
            print(json.dumps(compact(data), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
