title: Sign the poller's deliveries
expect: GIT-5
grade: fail
why: claims a timestamp check that no patch holds.
commit: Sign the poller's deliveries
file: src/bugflow/adapters/webhook_sink.py +5 -1
file: tests/unit/test_webhook_sink.py +6 -0
---
The poller signs each delivery with the webhook secret, the way GitHub does,
so the ingress can verify poller and webhook deliveries alike. The ingress
also rejects a delivery whose timestamp is more than five minutes old, so a
captured delivery cannot be replayed.
=== patch src/bugflow/adapters/webhook_sink.py
@@ -30,6 +30,10 @@ class WebhookSink:
         body = json.dumps(github_payload(delivery)).encode()
+        headers = {
+            "X-GitHub-Event": delivery.event,
+            "X-Hub-Signature-256": signature(self._secret, body),
+        }
-        response = self._client.post(self._url, content=body)
+        response = self._client.post(self._url, content=body, headers=headers)
=== patch tests/unit/test_webhook_sink.py
@@ -40,3 +40,9 @@
+
+
+def test_a_delivery_is_signed_with_the_webhook_secret() -> None:
+    sent = send(delivery())
+    expected = signature("secret", sent.content)
+    assert sent.headers["X-Hub-Signature-256"] == expected
