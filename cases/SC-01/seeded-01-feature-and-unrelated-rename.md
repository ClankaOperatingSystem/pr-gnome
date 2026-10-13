title: Add the stub judge and rename the replay command
expect: GIT-4
grade: fail
why: a feature and a rename with nothing in common but the branch.
commit: Add a stub judge that calls no model
commit: Rename the replay command to rehearse
file: src/bugflow/adapters/stub_judge.py +45 -0
file: tests/unit/test_stub_judge.py +40 -0
file: src/bugflow/app/cli.py +14 -14
file: Makefile +2 -2
---
The stub judge calls no model and finds nothing, so replay can run the
judge step offline. The replay command is renamed to rehearse.
