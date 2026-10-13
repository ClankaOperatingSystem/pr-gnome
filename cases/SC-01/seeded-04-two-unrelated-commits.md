title: Update the worker
expect: GIT-4
grade: fail
why: a command and a dependency bump with nothing in common but the branch.
commit: Add the dismissal command
commit: Bump the LiteLLM image to v1.101.0
file: src/bugflow/domain/dismissal.py +35 -0
file: src/bugflow/usecases/receive_delivery.py +60 -3
file: docker-compose.yml +1 -1
---
Adds the /dismiss comment command and moves LiteLLM to the next release.
