title: Keep the poll window after a refused delivery
expect: 
why: a fix with the test that pins it.
commit: Keep the poll window after a refused delivery
file: src/bugflow/usecases/poll_pull_requests.py +4 -2
file: tests/unit/test_poll_pull_requests.py +18 -0
---
A delivery the ingress refused moved the window forward, so it was never
posted again. The window now stays put when any delivery fails, and a test
refuses one delivery and checks the next poll reads the same window.
