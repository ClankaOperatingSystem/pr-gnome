title: Record dismissals as journal facts
expect: 
why: work named as left for later is not claimed by this diff.
commit: Record a dismiss comment as a journal fact
file: src/bugflow/domain/journal.py +1 -0
file: src/bugflow/domain/dismissal.py +14 -0
file: src/bugflow/usecases/receive_delivery.py +14 -0
---
A comment whose first line is /dismiss, a policy id and a reason is recorded
as a finding.dismissed entry in the journal, with the policy, the reason and
the comment's author.

The summary comment does not list dismissed findings yet, and they still
count for the label; that follows in its own pull request.
=== patch src/bugflow/domain/journal.py
@@ -22,6 +22,7 @@ EventType = Literal[
     "evaluation.completed",
     "judge.invoked",
     "findings.published",
+    "finding.dismissed",
 ]
=== patch src/bugflow/usecases/receive_delivery.py
@@ -118,6 +118,20 @@ class ReceiveDelivery:
         entries = [received_entry(delivery, outcome, occurred_at)]
+        dismissal = parse_dismissal(delivery.comment.body) if delivery.comment else None
+        if dismissal is not None:
+            entries.append(
+                JournalEntry(
+                    event_type="finding.dismissed",
+                    correlation=correlation,
+                    occurred_at=occurred_at,
+                    payload={
+                        "policy_id": dismissal.policy_id,
+                        "reason": dismissal.reason,
+                        "actor": delivery.comment.author,
+                    },
+                )
+            )
         self._journal.append(entries)
=== patch src/bugflow/domain/dismissal.py
@@ -0,0 +1,14 @@
+from dataclasses import dataclass
+
+
+@dataclass(frozen=True)
+class Dismissal:
+    policy_id: str
+    reason: str
+
+
+def parse_dismissal(body: str) -> Dismissal | None:
+    first = body.splitlines()[0].split(maxsplit=2) if body else []
+    if len(first) < 3 or first[0] != "/dismiss":
+        return None
+    return Dismissal(policy_id=first[1], reason=first[2])
