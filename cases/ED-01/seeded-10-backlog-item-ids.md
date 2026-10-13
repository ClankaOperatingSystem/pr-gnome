title: Stop a stocktake's run when its deadline passes
expect: VOICE-15
grade: fail
why: "C1.15" and "C1.16" stand in for the defects they name.
---
A weekly stocktake's review that was still running at its two-hour deadline was left running, where a pull request's review is stopped at its deadline. The stocktake now calls the same `review_stop` activity on the judge queue (cleanup.org C1.15).

It also records a second defect (cleanup.org C1.16). The fix for that is a choice between the runner reporting "in progress" as its own state and the stocktake waiting on a completion signal, which is already a todo.org item.
