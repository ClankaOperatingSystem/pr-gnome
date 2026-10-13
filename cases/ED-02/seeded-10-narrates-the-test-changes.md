title: Run the checked policy in a replay
expect: VOICE-2
grade: warn
why: narrates the test changes, which the diff shows.
commit: Run the checked policy in a replay
|
| The replay harness ran observe, judge and publish, and never the check,
| so ED-04, the em dash check, never reached a replay. It runs the check
| before judging and puts its findings first, as the evaluation workflow
| does, and its docstring names the steps it runs rather than an
| apply-policies use case that no longer exists.
|
| Closes C1.6 in cleanup.org.
file: cleanup.org +1 -1
file: src/bugflow/app/replay.py +28 -12
file: tests/unit/test_replay_harness.py +12 -5
---
Four replay tests pinned the harness without the check. They now expect the check's status in the judge status and its `policy.checked` fact in the journal. That fact carries the narrative agent's own corpus version, not the estate's, because the workflow stamps a checked finding that way; the corpus-version test says so rather than hiding it.
