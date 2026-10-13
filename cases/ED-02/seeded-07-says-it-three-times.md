title: Archive the judge's exchanges
expect: VOICE-2
grade: warn
why: the same fact stated three times.
commit: Archive the judge's exchanges
file: src/bugflow/adapters/sqlalchemy_judge_archive.py +40 -0
---
The request and the response are archived under the exchange id, so a
finding can be reproduced from its comment.

Under the exchange id, the request and the response are archived.

So the exchange id is where the request and the response are archived.
