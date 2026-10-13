title: Skip archived repositories when polling
expect: GIT-4
grade: warn
why: a feature and the fault its new test exposed; one led to the other.
commit: Skip archived repositories when polling
commit: Match repository names without case in the same filter
file: src/bugflow/usecases/poll_pull_requests.py +9 -3
file: tests/unit/test_poll_pull_requests.py +22 -0
---
Archived repositories are skipped rather than polled and then refused. The
repository filter also compared names case-sensitively, which the new test
for archived repositories tripped over, so the same filter now matches
without case as well.
