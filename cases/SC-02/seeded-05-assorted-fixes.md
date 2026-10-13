title: Assorted fixes to the poller
expect: GIT-4
grade: fail
why: "Assorted fixes" names a group and no change.
commit: Assorted fixes to the poller
file: src/bugflow/app/poller.py +64 -38
file: src/bugflow/usecases/poll_pull_requests.py +52 -26
file: tests/unit/test_poll_pull_requests.py +88 -30
---
The poller no longer reposts a delivery it has already sent, its interval is
read from the environment rather than hard coded, a comment whose author is
missing no longer raises, and the log line names the repository it polled.
