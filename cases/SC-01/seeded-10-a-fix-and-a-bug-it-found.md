title: Stop a stocktake's run when its deadline passes
expect: GIT-4
grade: warn
why: a fix and the bug found while making it; one led to the other.
commit: Stop a stocktake's run when its deadline passes
|
| The stocktake polled its run against a two-hour deadline and, when the
| deadline passed, ended without asking the runner to stop, so a session
| still going ran on and spent past the ceiling the deadline sets. The
| pull request's review stops its run in the same place. The stocktake
| now calls the same stop activity, on the judge's queue where the
| runner is, behind workflow.patched so runs in flight replay unchanged.
|
| Closes C1.15 in cleanup.org. Fixing it found C1.16, recorded there: a
| stocktake journals its run on the first poll, before it has ended.
file: cleanup.org +13 -1
file: src/bugflow/workflows/stocktake.py +17 -0
file: tests/unit/test_stocktake_workflow.py +56 -12
---
A weekly stocktake's review that was still running at its two-hour deadline was left running. The stocktake now calls the same stop activity as a pull request's review.

This also records a bug found while making the fix, and does not fix it: a stocktake journals its run on the first poll, before it has ended.
