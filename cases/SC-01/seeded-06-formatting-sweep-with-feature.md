title: Poll /dismiss comments
expect: GIT-4
grade: fail
why: a feature beside a formatting sweep.
commit: Poll /dismiss comments into the ingress
commit: Reformat the whole repository with the new line length
file: src/bugflow/usecases/poll_pull_requests.py +60 -10
file: tests/unit/test_poll_pull_requests.py +70 -0
file: src/bugflow/app/cli.py +40 -40
file: src/bugflow/adapters/github.py +80 -80
file: src/bugflow/workflows/pull_request.py +30 -30
file: pyproject.toml +1 -1
---
The poller posts /dismiss comments to the ingress. The line length goes
to 99 and the repository is reformatted to match.
