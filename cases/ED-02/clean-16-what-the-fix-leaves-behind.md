title: Leave no directory behind a review dispatch
expect:
why: states what the fix leaves behind and what to do about it.
commit: Leave no directory behind a review dispatch
|
| Every review dispatch created a temporary directory for a worktree and
| nothing removed it; the managed runner, the only one configured, mounts
| the repository itself and never read it. The path is now a name: a
| worktree service creates the directory when it prepares one.
|
| Closes C1.7 in cleanup.org.
file: cleanup.org +1 -1
file: src/bugflow/app/activities.py +7 -5
file: tests/unit/test_evaluation_activities_threading.py +16 -0
---
The worker's temporary directory has one empty `bugflow-review-*` directory for every review dispatched since the managed runner went in, and this does not remove them. They are safe to delete by hand.
