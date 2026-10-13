title: Rename the observe step to match the port
expect: 
why: one rename applied in six places.
commit: Rename the observe step to match the port
file: src/bugflow/usecases/observe_pull_request.py +12 -12
file: src/bugflow/workflows/evaluate_pull_request.py +6 -6
file: src/bugflow/app/activities.py +4 -4
file: src/bugflow/app/replay.py +3 -3
file: tests/unit/test_evaluation_steps.py +14 -14
file: tests/unit/test_replay_harness.py +5 -5
---
`fetch_pull_request` is called `observe_pull_request` everywhere, matching
the port it goes through and the journal entry it writes. One rename,
applied in six places.
