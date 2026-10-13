title: Bound the delivery queue
expect: VOICE-28
grade: warn
why: the opening clause has no comma, so "polls the queue" is formed first.
---
While the worker polls the queue fills. The queue now holds at most 500
deliveries and the ingress answers 503 when it is full.
