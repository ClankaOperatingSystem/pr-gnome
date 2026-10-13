title: Name the judge's model on a finding
expect: GIT-5
grade: warn
why: silent about renaming the public field judged_by.
commit: Name the judge's model on a finding
file: src/bugflow/domain/finding.py +2 -1
file: tests/unit/test_finding.py +2 -2
---
A judged finding carries the name of the model that made it, so a summary
comment can say which judge answered.
=== patch src/bugflow/domain/finding.py
@@ -18,4 +18,5 @@ class Finding(BaseModel):
     message: str
-    judged_by: str | None = None
+    judge: str | None = None
+    model: str | None = None
=== patch tests/unit/test_finding.py
@@ -8,4 +8,4 @@
-def test_a_finding_records_who_judged_it() -> None:
-    assert finding(judged_by="x").judged_by == "x"
+def test_a_finding_records_its_judge() -> None:
+    assert finding(judge="x").judge == "x"
