title: Poll every 60 seconds by default
expect: 
why: a changed default, and the description says so.
commit: Poll every 60 seconds by default
file: src/bugflow/app/poller.py +1 -1
file: .env.example +1 -1
---
Polling every 30 seconds spent a quarter of the GitHub rate limit on quiet
repositories. The default is now 60 seconds; POLL_INTERVAL still overrides
it.
=== patch src/bugflow/app/poller.py
@@ -18,7 +18,7 @@
-DEFAULT_INTERVAL = 30.0
+DEFAULT_INTERVAL = 60.0
=== patch .env.example
@@ -31,5 +31,5 @@
-# Seconds between polls. Default 30.
+# Seconds between polls. Default 60.
 POLL_INTERVAL=
