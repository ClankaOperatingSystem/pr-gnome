title: Move delivery signing into its own module
expect: 
why: a move whose function is unchanged, and the description says so.
commit: Move delivery signing into its own module
file: src/bugflow/adapters/webhook_sink.py +1 -8
file: src/bugflow/adapters/signing.py +8 -0
file: tests/unit/test_webhook_sink.py +1 -1
---
The ingress will verify signatures with the same function the poller signs
with, so signing moves out of the webhook sink into a module of its own. The
function is unchanged, and so is every delivery the poller sends.
=== patch src/bugflow/adapters/webhook_sink.py
@@ -1,20 +1,10 @@
-import hashlib
-import hmac
 import json

 import httpx2

+from bugflow.adapters.signing import signature
 from bugflow.domain.delivery import Delivery

-
-def signature(secret: str, body: bytes) -> str:
-    digest = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
-    return f"sha256={digest}"
-
-
 class WebhookSink:
=== patch src/bugflow/adapters/signing.py
@@ -0,0 +1,8 @@
+import hashlib
+import hmac
+
+
+def signature(secret: str, body: bytes) -> str:
+    digest = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
+    return f"sha256={digest}"
+
=== patch tests/unit/test_webhook_sink.py
@@ -3,7 +3,7 @@
-from bugflow.adapters.webhook_sink import signature
+from bugflow.adapters.signing import signature
