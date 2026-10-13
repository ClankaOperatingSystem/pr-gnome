title: Fix typos and add the exchanges table
expect: GIT-4
grade: fail
why: spelling fixes and a migration with nothing in common.
commit: Fix typos in index.org
commit: Create the judge_exchanges table
file: index.org +9 -9
file: migrations/versions/0003_create_judge_exchanges.py +40 -0
---
Corrects spelling across index.org and creates the table the judge's
exchanges will be archived in.
