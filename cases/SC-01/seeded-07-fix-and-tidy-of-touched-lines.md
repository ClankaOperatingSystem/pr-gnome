title: Keep the poll window after a refused delivery
expect: GIT-4
grade: warn
why: a fix and the tidy-up of the lines it touched; one led to the other.
commit: Keep the poll window after a refused delivery
commit: Rename the window helpers the fix touched
file: src/bugflow/usecases/poll_pull_requests.py +14 -9
file: tests/unit/test_poll_pull_requests.py +18 -0
---
A refused delivery moved the poll window forward; it now stays put. While
in there, the window helpers are renamed to say which end of the window
each one moves.
