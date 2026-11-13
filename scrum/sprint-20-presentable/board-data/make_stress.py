"""Make a stress data file for the board template: many items, three Sprints, two designs, English labels, long texts."""
import json
import sys

items = []
n = 0


def add(group, status, count, size="M"):
    global n
    for _ in range(count):
        n += 1
        items.append({
            "id": f"PBI-{n:03d}",
            "title": f"Item number {n}: a rather long title that keeps going to see how the overview truncates it" if n % 3 == 0 else f"Item {n}",
            "status": status, "size": size, "group": group,
        })


add("sprint", "In Sprint 07 (main)", 4)
add("sprint", "In Sprint 08 (side)", 3)
add("sprint", "In Sprint 09 (side)", 3)
add("design", "In design design-search (main)", 2)
add("design", "In design design-onboarding (side)", 1)
add("next", "Up next (side)", 5)
add("later", "Later", 6, "L")


def blocks(prefix_ids, total, done):
    out = []
    for i in range(total):
        pid = prefix_ids[i % len(prefix_ids)]
        out.append({"n": str(i + 1), "title": f"{pid}-{'a' if i % 2 == 0 else 'b'} work item {i + 1}", "done": i < done})
    return out


data = {
    "lang": "en",
    "generated": "2026-11-14 09:30",
    "product": {
        "name": "Harbour",
        "statement": "Harbour: a shared inbox that turns customer mail into tasks nobody has to copy by hand.",
        "goal": "Calm mornings: a support lead opens one page and sees what needs a reply, who owns it, and what is late.",
        "source": "working copy",
        "map": [
            {"text": "Mail arrives", "note": "1 · 2"},
            {"text": "Triage", "note": "3"},
            {"text": "Planning → Go-ahead → Build → Test", "here": ["sprint-07-intake", "sprint-08-search", "sprint-09-alerts"]},
            {"text": "Design sprint", "branch": True, "here": ["design-search", "design-onboarding"]},
            {"text": "Review → Retro"},
        ],
        "closed": 41,
    },
    "items": items,
    "sprints": [
        {"id": "sprint-07-intake", "goal": "Intake: every mail becomes a task with an owner within a minute.",
         "now": "Increment: blocks 1 to 6 done; block 7 under way.",
         "items": ["PBI-001", "PBI-002", "PBI-003", "PBI-004"], "blocks": blocks(["PBI-001", "PBI-002", "PBI-003", "PBI-004"], 22, 6), "source": "working copy"},
        {"id": "sprint-08-search", "goal": "Search: find any thread in under a second.",
         "now": "How: plan drafted, waiting for the go-ahead.",
         "items": ["PBI-005", "PBI-006", "PBI-007"], "blocks": blocks(["PBI-005", "PBI-006", "PBI-007"], 9, 0), "source": "branch sprint-08-search @ 3fa91c2"},
        {"id": "sprint-09-alerts", "goal": "Alerts: late tasks shout before the customer does.",
         "now": "What: refining.", "items": ["PBI-008", "PBI-009", "PBI-010"], "blocks": [], "source": "working copy"},
    ],
    "designs": [
        {"id": "design-search", "for": ["PBI-011", "PBI-012"], "goal": "Find out what people type when they look for a thread.",
         "now": "Prototype: three paper searches ready.", "map": ["Customer asks a question", "Agent looks for the old thread", "Agent gives up or finds it"],
         "story": [{"title": "Type", "text": "One box, any words."}, {"title": "See", "text": "Threads ranked by who answered last."}, {"title": "Open", "text": "One click to the thread."}],
         "source": "working copy", "ideo": [{"id": "ideo-words", "now": "Empathize: five interviews booked."}]},
        {"id": "design-onboarding", "for": ["PBI-013"], "goal": "Find out what a new agent needs in the first ten minutes.",
         "now": "Empathize: observing two new agents.", "map": ["New agent logs in", "Looks for their queue"], "story": [],
         "source": "branch design-onboarding @ 9b1d0aa"},
    ],
}
with open(sys.argv[1], "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("items", len(items))
