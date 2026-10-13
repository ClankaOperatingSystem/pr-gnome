title: Say plainly what the quota counts
expect:
why: the garden path is on a removed line, and the added line keeps its "that".
commit: Say plainly what the quota counts
file: src/judge/quota.py +1 -1
---
The comment read as "retries the judge" before it read as intended.
=== patch src/judge/quota.py
@@ -42,3 +42,3 @@ class Quota:
-        # Retries the judge drops count against the quota.
+        # A retry that the judge drops still counts against the quota.
         if call.reached_model or call.dropped:
