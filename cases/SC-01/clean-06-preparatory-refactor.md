title: Judge each policy in a request of its own
expect: 
why: a preparatory refactor with one purpose.
commit: Judge each policy in a request of its own
file: src/bugflow/adapters/litellm_judge.py +120 -80
file: src/bugflow/usecases/judge_pull_request.py +70 -40
file: src/bugflow/ports/judge.py +12 -2
file: tests/unit/test_judge_policies.py +130 -0
---
The judge holds a set of policies, each judged in a request of its own,
so the next policy can see commits that editorial voice does not. The use
case records a judge.invoked entry per policy.
