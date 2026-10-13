title: Add the dismissal command
expect: 
why: a feature with its tests and documentation, which are derived.
commit: Add the dismissal command
file: src/bugflow/usecases/receive_delivery.py +64 -3
file: tests/unit/test_receive_delivery.py +112 -0
file: index.org +34 -1
---
A comment whose first line is `/dismiss <policy-id> <reason>` records
`finding.dismissed` and starts an evaluation. Its tests and the section of
index.org that describes it come with it.
