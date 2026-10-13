title: Give the judge a rate limit
expect: 
why: a preparatory commit, then the commit that needs it.
commit: Take the judge's queue name from settings
commit: Rate limit the judge's queue
file: src/bugflow/app/temporal.py +26 -8
file: src/bugflow/app/worker.py +34 -6
file: tests/unit/test_worker_composition.py +72 -0
file: .env.example +6 -0
---
The judge runs on its own task queue so its rate limit is separate from the
forge's. The first commit takes the queue's name from settings, which the
second needs in order to set a limit on it.
