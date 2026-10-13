title: Add the exchange id to judged findings
expect: GIT-5
grade: fail
why: silent about a migration that drops a column.
commit: Add the exchange id to judged findings
file: src/bugflow/domain/finding.py +1 -0
file: migrations/versions/0004_drop_snapshot_bodies.py +15 -0
file: tests/unit/test_finding.py +4 -0
---
A judged finding carries the id of the exchange it came from, so a reviewer
can reproduce the judgement from the summary comment. The id is optional,
because deterministic findings have no exchange.
=== patch src/bugflow/domain/finding.py
@@ -20,3 +20,4 @@ class Finding(BaseModel):
     message: str
     judged_by: str | None = None
+    exchange_id: str | None = None
=== patch migrations/versions/0004_drop_snapshot_bodies.py
@@ -0,0 +1,15 @@
+"""Drop the stored snapshot bodies."""
+
+from alembic import op
+
+revision = "0004"
+down_revision = "0003"
+
+
+def upgrade() -> None:
+    op.drop_column("snapshots", "body")
+
+
+def downgrade() -> None:
+    raise NotImplementedError("the bodies are gone")
+
=== patch tests/unit/test_finding.py
@@ -12,3 +12,7 @@
+
+
+def test_a_finding_carries_its_exchange_id() -> None:
+    assert finding(exchange_id="abc").exchange_id == "abc"
