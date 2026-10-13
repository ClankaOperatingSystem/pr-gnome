title: Back off when the judge is rate limited
expect: 
why: states the problem, the decision and a rejected option, none of which the diff shows.
commit: Back off when the judge is rate limited
file: src/bugflow/adapters/litellm_judge.py +40 -6
file: tests/unit/test_litellm_judge.py +55 -0
---
A 429 from the model failed the evaluation outright, so a busy minute lost a judgement. The adapter now reports how long to wait, taken from Retry-After, else the retryDelay in the body, else a minute, and the activity waits that long. Rejected: retrying inside the adapter, which would hide the wait from the workflow's history.
