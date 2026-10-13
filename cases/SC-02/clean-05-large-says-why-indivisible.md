title: Move the policy package behind the judge
expect: 
why: a large commit whose description says why it cannot be split.
commit: Move the policy package behind the judge
file: src/bugflow/policy/__init__.py +0 -312
file: src/bugflow/policy/deterministic.py +0 -410
file: src/bugflow/usecases/evaluate_pull_request.py +62 -140
file: src/bugflow/app/worker.py +18 -44
file: tests/unit/test_evaluation_steps.py +90 -260
file: index.org +40 -22
---
The eight deterministic policies are retired, so the policy package, the
apply-policies step and its activity go, and an evaluation's findings all
come from the judge.

This cannot be a sequence. The step, the activity and the package reference
one another, and removing any one of them alone leaves imports that do not
resolve and a worker that will not start.
