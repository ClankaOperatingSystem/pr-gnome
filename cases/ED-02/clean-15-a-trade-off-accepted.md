title: Judge an edited description again
expect:
why: states a trade-off the change accepts.
commit: Judge an edited description again
|
| The evaluation skips judging what it has already judged, and asked
| whether this commit had been judged under this corpus. An edit to the
| title or description changes neither, so every edit was skipped as a
| duplicate, and an author who fixed a flagged sentence never saw the
| finding cleared: five of the seven policies judge the description.
|
| The skip now asks whether this snapshot was judged under this corpus.
| The snapshot's content hash covers the title, the description, the
| commits and the patches, and every judgement records it, so two
| deliveries of one push still judge once and an edit judges again.
file: src/bugflow/forge/usecases/observe_pull_request.py +11 -10
file: tests/unit/test_evaluation_steps.py +24 -8
file: todo.org +7 -0
---
The snapshot also carries the base commit, so a push whose webhook and polled copies straddle a merge to master is judged twice. That costs one evaluation's tokens and was judged not worth a narrower key.
