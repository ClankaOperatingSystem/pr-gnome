title: Count dropped retries against the quota
expect:
why: the article and the "that" settle the reading.
commit: Count dropped retries against the quota
file: src/judge/quota.py +3 -1
---
A retry the judge drops now counts against the quota.
=== patch src/judge/quota.py
@@ -41,5 +41,7 @@ class Quota:
     def spend(self, call: Call) -> None:
-        if call.reached_model:
+        # A retry that the judge drops still counts against the quota.
+        if call.reached_model or call.dropped:
+            self._calls += 1
             self._used += call.cost
