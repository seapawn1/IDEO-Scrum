"""准备 Sprint 21 H3 的同数据对照页与独立读卡材料。

取得运行放行后，可从任意目录调用本脚本的绝对路径，例如：
    python -I /绝对路径/prepare_review.py --baseline <旧提交或分支> --out <全新或空目录>

本工具只复制夹具和生成材料，不运行检查、浏览器、模型评阅或测试。
两页使用同一次 reference_data 的结果；旧模板必须由 --baseline 明确指定。
仅访问脚本所在工作树的工具、夹具、模板和 git 对象，不取实际项目日志或主检出。
不清理或覆盖输出；中途失败留下的材料保留，下次应另选全新或空目录。
生成材料不表示已通过验收，也不表示 Test 已放行。
"""

import argparse
import importlib.util
import json
import pathlib
import shutil
import subprocess
import sys


HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
FIXTURE = HERE / "fixtures" / "acme"
EXPECTATIONS = HERE / "fixtures" / "review-expectations.json"
TEMPLATE_PATH = "plugins/ideo-scrum/skills/scrum-kernel/conventions/scrum-board-template.html"

BLIND_TASK = """# 独立读卡任务

只看 current 页面里的 B 卡（feedback-sample）：
[打开这张卡](current/scrum/ScrumBoard.html#design-feedback-sample)

请仅凭这张可见卡片回答；不要打开日志、页面源码、其他卡片或其他材料，也不要听作者解释。
不需要猜作者的意思，卡上看不出的地方就写「看不出」。

| 问题 | 你的回答 |
| --- | --- |
| 这次设计选了什么？ | |
| 如果要使用它，你会怎么做？ | |
| 按卡片这样使用之后，接下来会发生什么？ | |

请保留你的原话，并指出哪些信息是卡上说清楚的，哪些没有说清楚。
"""

CHECKLIST = """# 作者复核清单

本文件与 review-expectations.json 只给作者，不交给独立读卡评阅者。
这是 Sprint 21 §2.2 既有口径的执行提示，不是测试结果，也不增加验收标准。
生成 HTML、JSON 非空或字段齐全都不表示页面已通过；各项目前均待实际复核。
正式 Test 仍须另行放行，本工具不会启动任何复核。

## 材料与盲读隔离

| 材料 | 用途 |
| --- | --- |
| current/scrum/ScrumBoard.html | 当前工作树模板生成的页面 |
| baseline/scrum/ScrumBoard.html | --baseline 指定的旧模板生成的页面 |
| review-expectations.json | 从源夹具核定的 A/B/C 目标、路线、选定状态与必要语义，仅供作者对账 |
| blind-read-task.md | 给独立评阅者的任务，只指向 current 的 B 卡，不带答案或日志链接 |

本次 --baseline 的输入是 BASELINE_REF。
baseline 只是旧模板对照，不代表旧提交中的日志或旧数据；两份项目都完整复制同一份 fixtures/acme，
两页共用一次 reference_data(acme, ACME_SUMM) 的 JSON，没有为旧模板改写数据或补故事板。
两份副本的日志与原始夹具均不改写。

将 blind-read-task.md 与 current 的 B 卡交给独立评阅者，只让其看卡片可见内容。
不要把本清单、期待 JSON、源日志、baseline 或页面源码交给该评阅者，也不要口头解释方案。
先保留独立回答，再按期待 JSON 与源夹具核对；无法从卡片读出的内容按实际记录，不代答、不补讲。

## A/B/C 内容对账

| 场景 | current 中待核内容 | 口径 |
| --- | --- | --- |
| A · design-gamma | 目标逐字相同；地图主线沿源图顺序；选定方案独立可见，并与可选故事板相符 | 故事板帮助理解，不替代方案 |
| B · design-feedback-sample | 目标、路线与源夹具一致；没有单独故事板，方案仍可见；独立读卡回答能与 §3.1 的必要语义对上 | 只看卡，不听讲解；按意思核，不要求复述固定句子 |
| C · design-choosing | 目标、路线与源夹具一致；方案区仍在，能看出尚未选定；候选没有被写成定案 | 不固定空态用词，不要求展示候选草图 |

期待 JSON 的 source 路径相对每份项目根目录；必要语义的引文来自该夹具，而非生成页面。
B 只摘归档 §3.1，不补故事板，不移动或改写归档，不把原设计当作在办项目。
不要把未在源文写明的用法、选定理由、布局或故事板帧数加成通过线。

## 同数据核对两类非设计卡

用手工操作或浏览器工具，在相同宽度、主题、卡片和交互状态下比较，
核真实可见的外观、内容与交互；不能只看两页的数据相同就判定无回归。

| 对照 | current | baseline |
| --- | --- | --- |
| 产品卡 | current/scrum/ScrumBoard.html#product | baseline/scrum/ScrumBoard.html#product |
| 普通 Sprint 卡 | current/scrum/ScrumBoard.html#sprint-01-alpha | baseline/scrum/ScrumBoard.html#sprint-01-alpha |

## 既有页面约束

| 待核项目 | 操作提示 |
| --- | --- |
| 三档宽度 | 分别用 1440、900、375 CSS 像素宽度查看两页；这是观察宽中窄的取样，不是规定布局断点 |
| light / dark | 每档宽度均观察浅色与深色；用系统设置或浏览器主题模拟切换，确认页面确实进入相应主题 |
| 离线 | 直接从本地打开页面，在断网或浏览器离线状态下重新打开，核页面及操作仍可用 |
| 可见性 | 实际打开 A/B/C 卡、滚动及展开相关内容，核信息可读、未被遮住或截掉；源码、隐藏 DOM 和字段存在不能替代可见性证据 |
| 导航 | 点击产品圆圈、条目和 Sprint／设计节点，核原有高亮、开卡、返回总览及窄屏切换，不因设计卡改动回归 |
| Now | 实际展开卡脚的 Now，与该副本日志的 > Now: 原文核对，不从方案摘要反推 |
| 来源与链接 | 核卡脚的文件夹名和来源；working copy 链接在同一份副本里能打开；若出现仅在分支上的来源，只标分支和提交，不伪造本地链接 |

本工具只生成 working copy 夹具材料，不制造仅在分支上的日志场景。
记录实际观察的宽度、主题、操作、截图或读卡原话及发现的问题；未执行的写「未核」，不自动填通过。
"""


def load_checker():
    """按本脚本绝对位置加载工具，兼容 -I，且不向源目录写字节码。"""
    path = HERE / "check.py"
    spec = importlib.util.spec_from_file_location("_board_check_review", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("无法加载本工作树的 check.py。")
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    try:
        sys.dont_write_bytecode = True
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def baseline_template(baseline):
    """只读指定 git 对象中的旧模板，不切分支，也不接触主检出。"""
    result = subprocess.run(
        ["git", "-C", str(REPO), "show", "--end-of-options", baseline + ":" + TEMPLATE_PATH],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode:
        raise ValueError("无法读取 --baseline 的旧模板：" + result.stderr.strip())
    return result.stdout


def output_directory(value):
    """只接受全新或空目录，拒绝指向目录的符号链接和源夹具内部路径。"""
    path = pathlib.Path(value).expanduser()
    if path.is_symlink():
        raise ValueError("--out 不能是符号链接。")
    path = path.resolve()
    if path == FIXTURE or FIXTURE in path.parents:
        raise ValueError("--out 不能位于源夹具内部。")
    require_empty(path)
    return path


def require_empty(path):
    """输出目录含有任何内容时拒绝，不清理、不合并。"""
    if path.exists():
        if not path.is_dir():
            raise ValueError("--out 已存在且不是目录：" + str(path))
        if next(path.iterdir(), None) is not None:
            raise ValueError("--out 必须全新或为空，已有内容将保留：" + str(path))


def write_new(path, text):
    """以 UTF-8 独占新建文件，避免意外覆盖后来出现的内容。"""
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(text)


def prepare(out, baseline):
    """复制两份项目，用同一份数据生成对照页及作者、评阅者各自的材料。"""
    checker = load_checker()
    current_text = (REPO / TEMPLATE_PATH).read_text(encoding="utf-8")
    baseline_text = baseline_template(baseline)
    expectations_text = EXPECTATIONS.read_text(encoding="utf-8")
    json.loads(expectations_text)
    for label, template in (("当前", current_text), ("旧版", baseline_text)):
        if template.count(checker.PLACEHOLDER) != 1:
            raise ValueError(label + "模板没有唯一的数据占位行，不能生成；不会修改模板以迁就数据。")

    # 输入材料读完后再建目录；写入前重查，出现内容即停，不删除任何产物。
    out.mkdir(parents=True, exist_ok=True)
    require_empty(out)
    current = out / "current"
    previous = out / "baseline"
    shutil.copytree(FIXTURE, current)
    shutil.copytree(FIXTURE, previous)

    # 只调用一次参考生成；两页共用该对象，不为旧模板移除或改写字段。
    data = checker.reference_data(current, checker.ACME_SUMM)
    current_page = checker.make_page(data, current_text)
    previous_page = checker.make_page(data, baseline_text)
    write_new(current / "scrum" / "ScrumBoard.html", current_page)
    write_new(previous / "scrum" / "ScrumBoard.html", previous_page)
    write_new(out / "review-expectations.json", expectations_text)
    write_new(out / "review-checklist.md", CHECKLIST.replace("BASELINE_REF", repr(baseline)))
    write_new(out / "blind-read-task.md", BLIND_TASK)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--baseline", required=True, help="含旧模板的明确提交或分支，必填。")
    parser.add_argument("--out", required=True, help="生成材料的全新或空目录，已有内容时拒绝。")
    args = parser.parse_args()
    if not args.baseline.strip():
        parser.error("--baseline 不能为空。")
    try:
        out = output_directory(args.out)
        prepare(out, args.baseline)
    except (OSError, ValueError, RuntimeError, AssertionError, ImportError, AttributeError, TypeError) as exc:
        print("材料未完整生成；不清理或覆盖已有内容：" + str(exc), file=sys.stderr)
        return 1
    print("材料已生成，尚未运行任何验收：" + str(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
