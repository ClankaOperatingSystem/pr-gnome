title: Store the judge's exchanges
expect: GIT-4
grade: fail
why: "This also adds" names a second reason in the description.
commit: Store the judge's exchanges
file: src/bugflow/adapters/sqlalchemy_judge_archive.py +140 -0
file: migrations/versions/0007_judge_exchanges.py +34 -0
file: tests/integration/test_judge_archive.py +90 -0
file: src/bugflow/app/cli.py +46 -2
file: tests/unit/test_policy_catalogue.py +12 -0
---
Every request sent to a model and the response it gave are archived under an
exchange id, which each judged finding records, so a finding can be
reproduced from what was actually sent.

This also adds the `policies` command, which prints the catalogue of judged
policies and where each one's calibration stands.
