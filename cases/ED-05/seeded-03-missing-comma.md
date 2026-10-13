title: Bound the delivery queue
expect: VOICE-28
grade: warn
why: the opening clause has no comma, so "polls the queue" is formed first.
commit: Bound the delivery queue
file: src/ingress/queue.py +3 -1
---
The queue holds at most 500 deliveries, and the ingress answers 503 when
it is full.
=== patch src/ingress/queue.py
@@ -12,4 +12,6 @@ from collections import deque

-QUEUE: deque[Delivery] = deque()
+# While the worker polls the queue fills. Nothing bounded it before.
+LIMIT = 500
+QUEUE: deque[Delivery] = deque(maxlen=LIMIT)
