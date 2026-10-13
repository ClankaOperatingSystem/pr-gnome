title: Add the poller and fix the label removal
expect: GIT-4
grade: fail
why: a feature and a fix in one commit, each with a reason of its own.
commit: Add the poller and fix the label removal
file: src/bugflow/app/poller.py +130 -0
file: tests/unit/test_poll_pull_requests.py +148 -0
file: src/bugflow/adapters/github.py +6 -4
file: tests/conformance/test_forge_conformance.py +18 -0
---
The poller reads pull requests with the forge token and posts them to the
ingress as signed deliveries. The label removal sent the whole managed set
rather than the labels the pull request carries, which GitHub answers 404
for, and that is corrected here.
