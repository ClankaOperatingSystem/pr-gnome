title: Poll pull requests into the ingress
expect: 
why: a counted test result is a measurement, and the rest is plain description.
---
Webhooks to the ingress are the design, but a forge cannot reach an ingress
on a laptop. The poller stands in for the webhook there.

It lists the watched repositories' pull requests and posts each change to the
ingress as a signed `pull_request` delivery. A delivery's id is derived from
the head commit, title and description, so the ingress drops an unchanged
pull request as a duplicate.

`make check`: 303 passed, 27 of them new.
