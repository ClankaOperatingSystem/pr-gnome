title: Poll pull requests into the ingress
expect: 
why: a feature with the tests, compose service and documentation it needs.
commit: Poll pull requests into the ingress
file: src/bugflow/app/poller.py +120 -0
file: src/bugflow/usecases/poll_pull_requests.py +95 -0
file: tests/unit/test_poll_pull_requests.py +140 -0
file: index.org +30 -2
file: docker-compose.yml +18 -0
---
The poller lists the watched repositories' pull requests and posts each
change to the ingress as a signed delivery. Its compose service, tests and
the index.org section that describes it come with it.
