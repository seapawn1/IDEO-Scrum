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


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--suites", nargs="+", default=["baseline", "revised"])
    parser.add_argument("--answers", nargs="*")
    args = parser.parse_args()
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
