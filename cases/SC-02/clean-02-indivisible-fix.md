title: Pass the snapshot by reference through the workflow
expect: 
why: a fix whose parts would not build apart, and the description says so.
commit: Pass the snapshot by reference through the workflow
file: src/bugflow/workflows/evaluate_pull_request.py +84 -61
file: src/bugflow/usecases/observe_pull_request.py +96 -40
file: src/bugflow/usecases/publish_findings.py +38 -22
file: src/bugflow/adapters/sqlalchemy_snapshots.py +210 -0
file: tests/unit/test_snapshot_references.py +180 -0
---
A large pull request's snapshot exceeded Temporal's payload limit when it
passed between activities. The snapshot is now stored once and passed as a
content-hash reference, which every step resolves through the snapshot port.

The store, the port, the workflow's plumbing and the steps that read the
snapshot change together. Splitting them leaves a build where one activity
sends a reference and the next expects a snapshot, which does not run.
