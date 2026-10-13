title: Edit the summary comment in place
expect: 
why: work the description says was done earlier is not claimed by this diff.
commit: Edit the summary comment in place
file: src/bugflow/usecases/publish_findings.py +5 -1
file: src/bugflow/ports/forge.py +6 -0
file: src/bugflow/adapters/github.py +22 -0
file: tests/unit/test_publish_findings.py +31 -2
---
Pull request 38 made publishing post a summary comment, and it posts a new
one on every evaluation, so a busy pull request collects a stack of them.
Publishing now finds the earlier summary by its marker and edits it, and
posts a new one only when there is none.
=== patch src/bugflow/usecases/publish_findings.py
@@ -64,7 +64,13 @@ class PublishFindings:
         body = render_summary(request, resolved, dismissals)
-        self._forge.create_comment(request.ref, body)
+        existing = self._forge.find_comment(request.ref, SUMMARY_MARKER)
+        if existing is None:
+            self._forge.create_comment(request.ref, body)
+        else:
+            self._forge.edit_comment(request.ref, existing, body)
         self._forge.set_label(request.ref, label)
=== patch src/bugflow/ports/forge.py
@@ -40,3 +40,9 @@ class ForgePublisherPort(Protocol):
     def create_comment(self, ref: PullRequestRef, body: str) -> int: ...
+
+    def find_comment(self, ref: PullRequestRef, marker: str) -> int | None: ...
+
+    def edit_comment(
+        self, ref: PullRequestRef, comment_id: int, body: str
+    ) -> None: ...
