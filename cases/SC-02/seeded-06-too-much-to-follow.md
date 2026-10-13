title: Add the fleet rollout workflow
expect: GIT-4
grade: warn
why: one reason in parts that no reviewer can follow as a whole.
commit: Add the fleet rollout workflow
file: src/bugflow/workflows/policy_rollout.py +620 -0
file: src/bugflow/usecases/roll_out_policy.py +430 -0
file: src/bugflow/adapters/stub_rollout_target.py +180 -0
file: src/bugflow/ports/rollout.py +90 -0
file: src/bugflow/app/worker.py +120 -14
file: src/bugflow/app/cli.py +160 -4
file: tests/unit/test_policy_rollout_workflow.py +540 -0
file: tests/unit/test_roll_out_policy.py +380 -0
file: index.org +190 -12
---
The rollout workflow canaries a subset of repositories, pauses on a signal,
resumes on another, reports progress on a query, and continues as new between
waves. It comes with its port, a stub target, the worker's registration, the
command that starts it and the tests for all of it.
