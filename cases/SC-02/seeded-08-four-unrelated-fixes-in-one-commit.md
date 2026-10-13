title: Fix replay, the quarterly cadence and a leaked directory
expect: GIT-4
grade: fail
why: four defects in one commit, each with a reason of its own.
commit: Fix replay, the quarterly cadence and a leaked directory
|
| Four defects the whole-repository stocktake found, each in the app
| layer:
|
| - bugflow replay refused its default doctrine, a directory, because it
|   checked for a file, so make replay exited 2. It now accepts either,
|   as the reader it hands the path to already did.
| - The replay harness never ran the checked policy, so ED-04 never
|   reached a replay. It runs the check before judging and merges its
|   findings first, as the evaluation workflow does.
| - The quarterly cadence fired on 1 January only, the same calendar as
|   annual. It fires in January, April, July and October.
| - Every review dispatch created an empty temporary directory and
|   nothing removed it. The path is now a name: a worktree service
|   creates the directory when it prepares one, and a runner that mounts
|   the repository never reads it.
|
| Closes C1.4 to C1.7 in cleanup.org.
file: cleanup.org +4 -4
file: src/bugflow/app/activities.py +7 -5
file: src/bugflow/app/cli.py +1 -1
file: src/bugflow/app/replay.py +28 -12
file: src/bugflow/app/schedules.py +6 -4
file: tests/unit/test_evaluation_activities_threading.py +16 -0
file: tests/unit/test_replay_harness.py +25 -5
file: tests/unit/test_what_a_cadence_schedules.py +8 -0
---
Four defects from the whole-repository stocktake, each with a test that fails without its fix.
