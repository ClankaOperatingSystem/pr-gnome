title: Fix the poller's window and tidy logging
expect: GIT-4
grade: fail
why: a fix and a logging refactor elsewhere.
commit: Keep the poll window after a refused delivery
commit: Replace print calls with the logging module
file: src/bugflow/usecases/poll_pull_requests.py +4 -2
file: tests/unit/test_poll_pull_requests.py +18 -0
file: src/bugflow/app/worker.py +12 -9
file: src/bugflow/app/ingress.py +8 -3
---
A refused delivery moved the poll window forward; the window now stays
put. The worker and the ingress also move from print to the logging
module.
