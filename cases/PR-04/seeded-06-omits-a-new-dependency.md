title: Parse dismissal comments
expect: GIT-5
grade: warn
why: silent about the regex dependency the patch adds.
commit: Parse dismissal comments
file: src/bugflow/domain/dismissal.py +18 -0
file: pyproject.toml +1 -0
file: tests/unit/test_dismissal.py +24 -0
---
A comment's first line, /dismiss followed by a policy id and a reason, is
parsed into a dismissal. A comment with no reason, or whose first line is
anything else, is not a dismissal.
=== patch src/bugflow/domain/dismissal.py
@@ -0,0 +1,18 @@
+"""A reviewer's dismissal of a finding, read from a comment."""
+
+import regex
+
+from pydantic import BaseModel
+
+_COMMAND = regex.compile(r"^/dismiss\s+(\p{Lu}+-\d+)\s+(\S.*)$")
+
+
+class Dismissal(BaseModel):
+    policy_id: str
+    reason: str
+
+
+def parse_dismissal(text: str) -> Dismissal | None:
+    match = _COMMAND.match(text.splitlines()[0] if text else "")
+    return Dismissal(policy_id=match[1], reason=match[2]) if match else None
+
=== patch pyproject.toml
@@ -14,6 +14,7 @@ dependencies = [
     "pydantic>=2.7",
+    "regex>=2024.11",
     "sqlalchemy>=2.0",
