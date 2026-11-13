"""Make a board page from the template and a data file, for the screenshots and the checks.

usage: python -X utf8 -I make_page.py DATA.json OUT.html [TEMPLATE.html]

The template holds one placeholder line inside <script id="board-data">; the data replaces it, with every "<" written
as a backslash u003c escape, which is what board-log.md asks of whoever writes a real page.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_TEMPLATE = HERE.parents[2] / "plugins/ideo-scrum/skills/scrum-kernel/conventions/scrum-board-template.html"
PLACEHOLDER = '{"todo": "Replace this line with the board data (board-log.md lists the fields)."}'

data_path, out_path = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
template = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_TEMPLATE
text = template.read_text(encoding="utf-8")
assert text.count(PLACEHOLDER) == 1, "the template must hold the placeholder line exactly once"
data = json.loads(data_path.read_text(encoding="utf-8"))
block = json.dumps(data, ensure_ascii=False, indent=1).replace("<", chr(92) + "u003c")
out_path.write_text(text.replace(PLACEHOLDER, block), encoding="utf-8")
print("wrote", out_path)
