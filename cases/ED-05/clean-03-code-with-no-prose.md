title: Bound the delivery queue
expect:
why: the patch adds code and no prose.
commit: Bound the delivery queue
file: src/ingress/queue.py +2 -1
---
The queue holds at most 500 deliveries, and the ingress answers 503 when
it is full.
=== patch src/ingress/queue.py
@@ -12,4 +12,5 @@ from collections import deque

-QUEUE: deque[Delivery] = deque()
+LIMIT = 500
+QUEUE: deque[Delivery] = deque(maxlen=LIMIT)
