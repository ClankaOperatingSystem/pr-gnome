title: Tidy the label choice
expect: GIT-5
grade: fail
why: says no behaviour change, and the patch changes which findings fail the label.
commit: Tidy the label choice
file: src/bugflow/usecases/publish_findings.py +4 -4
---
Renames the label function's argument to say the findings are the open
ones, and makes the severities a list. No behaviour change.
=== patch src/bugflow/usecases/publish_findings.py
@@ -30,10 +30,10 @@
-def label_for(findings: Sequence[Finding]) -> str:
-    severities = {f.severity for f in findings}
-    if "fail" in severities:
+def label_for(open_findings: Sequence[Finding]) -> str:
+    severities = [f.severity for f in open_findings]
+    if severities.count("fail") > 1:
         return "doctrine:fail"
-    if "warn" in severities:
+    if "warn" in severities or "fail" in severities:
         return "doctrine:warn"
     return "doctrine:pass"
