"""Screenshot a board page at 1440 wide and at a true 375 wide, and report sideways overflow.

    python shot.py <page.html> <out-prefix>

Writes <out-prefix>-1440.png and <out-prefix>-375.png and prints, for each width, whether the page
overflows sideways (68-2). The 375 shot is the page inside a 375-wide iframe: with --window-size=375
alone, Edge headless laid the first board out wider than the window and cut its right side off.
"""
import html
import json
import pathlib
import re
import subprocess
import sys

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]
SCREEN = {1440: 900, 375: 812}  # screen heights used when measuring
WRAP = """<!doctype html><meta charset="utf-8">
<body style="margin:0;background:#8a8a8a">
<iframe id="f" src="{src}" width="{w}" height="{h}" style="border:0;background:#fff;display:block;margin:0 auto"></iframe>
<script>
var f = document.getElementById('f');
f.addEventListener('load', function () {{ setTimeout(function () {{
  try {{
    var d = f.contentDocument.documentElement;
    document.body.setAttribute('data-r', JSON.stringify({{sw: d.scrollWidth, cw: d.clientWidth, sh: d.scrollHeight}}));
  }} catch (e) {{ document.body.setAttribute('data-r', 'ERR ' + e); }}
}}, 800); }});
</script>
"""


def browser():
    for b in BROWSERS:
        if pathlib.Path(b).is_file():
            return b
    sys.exit("no Edge or Chrome found")


def run(args):
    cmd = [browser(), "--headless", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files"] + args
    return subprocess.run(cmd, capture_output=True, timeout=180)


def one(page_url, prefix, width):
    wrap = prefix.with_name(f"{prefix.name}-wrap-{width}.html")
    try:
        # 1. measure: an iframe as tall as a real screen (so 100vh means what it should), then take
        #    scrollHeight: the page's own height, or the screen's if the page is shorter
        wrap.write_text(WRAP.format(src=page_url, w=width, h=SCREEN[width]), encoding="utf-8")
        dom = run(["--virtual-time-budget=4000", "--dump-dom", wrap.as_uri()]).stdout.decode("utf-8", "replace")
        m = re.search(r'data-r="([^"]*)"', dom)
        if not m or m.group(1).startswith("ERR"):
            return f"{width}: could not measure ({m.group(1) if m else 'no result'})"
        r = json.loads(html.unescape(m.group(1)))
        # 2. shoot: an iframe as tall as the page
        height = r["sh"]
        wrap.write_text(WRAP.format(src=page_url, w=width, h=height), encoding="utf-8")
        out = prefix.with_name(f"{prefix.name}-{width}.png")
        run([f"--screenshot={out}", f"--window-size={max(width, 600)},{height}", wrap.as_uri()])
        side = "SIDEWAYS OVERFLOW" if r["sw"] > r["cw"] else "no sideways overflow"
        return f"{width}: scrollWidth {r['sw']} / clientWidth {r['cw']} -> {side}; page height {height}; {out}"
    finally:
        wrap.unlink(missing_ok=True)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    page = pathlib.Path(sys.argv[1]).resolve()
    prefix = pathlib.Path(sys.argv[2]).resolve()
    prefix.parent.mkdir(parents=True, exist_ok=True)
    for width in (1440, 375):
        print(one(page.as_uri(), prefix, width))


if __name__ == "__main__":
    main()
