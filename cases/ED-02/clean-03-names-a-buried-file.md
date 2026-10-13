title: Add the exchange id to findings
expect: 
why: names the migration, which a reviewer would otherwise miss, and what its rule means.
commit: Add the exchange id to judged findings
file: src/bugflow/domain/finding.py +2 -0
file: migrations/versions/0004_add_exchange_id.py +18 -0
file: tests/unit/test_finding.py +9 -0
---
A finding now carries the id of the exchange it came from, so a reviewer can reproduce the judgement. Note the migration: 0004 adds a nullable column, and the journal's additive rule means it is never backfilled.
