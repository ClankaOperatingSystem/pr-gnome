title: Record the judge's identity
expect: GIT-4
grade: fail
why: "also adds pagination" names a second purpose in the description.
commit: Record the identity of every judgement
file: src/bugflow/domain/judgement.py +50 -0
file: src/bugflow/usecases/judge_pull_request.py +40 -10
file: migrations/versions/0003_create_judge_exchanges.py +40 -0
file: src/bugflow/adapters/github.py +30 -5
---
Each judged finding records the model, the prompt hash and the exchange it
came from. This also adds pagination to the GitHub adapter's comment
listing.
