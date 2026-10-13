title: Document the dismiss command
expect: 
why: a documentation change with nothing claimed beyond it.
commit: Document the dismiss command
file: index.org +8 -0
---
The dismiss command had no documentation outside the task that built it.
index.org now says how to dismiss a finding, that a reason is required, and
what the summary and label do with it.
=== patch index.org
@@ -2140,6 +2140,14 @@ the journal to the published comment.
 - [X] Dismissal signal: the /dismiss comment command as a journal fact.
+
+** Dismissing a finding
+
+A reviewer who disagrees with a finding comments on the pull request with
+=/dismiss <policy-id> <reason>= as the comment's first line. The reason is
+required. The finding moves under Dismissed in the summary comment and no
+longer counts for the label. Dismissing is recorded, never deleted: the
+journal keeps the finding and the dismissal both.
