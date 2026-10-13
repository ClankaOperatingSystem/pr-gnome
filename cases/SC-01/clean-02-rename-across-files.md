title: Rename the evaluate command to assess
expect: 
why: one rename applied everywhere it is referenced.
commit: Rename the evaluate command to assess
file: src/bugflow/app/cli.py +12 -12
file: Makefile +3 -3
file: index.org +6 -6
file: tests/unit/test_cli.py +9 -9
---
The command evaluates nothing itself; it asks the worker to assess a pull
request. Every reference to the old name is renamed.
