title: Skip draft pull requests in the poller
expect: 
why: the description claims a feature and a test, and the patches hold both.
commit: Skip draft pull requests in the poller
file: src/bugflow/domain/polling.py +1 -0
file: src/bugflow/usecases/poll_pull_requests.py +2 -0
file: src/bugflow/adapters/github.py +1 -0
file: tests/unit/test_poll_pull_requests.py +7 -0
---
The poller no longer posts a delivery for an open draft pull request, so a
draft is not evaluated until it is marked ready for review. GitHub's draft
flag is read from the pull request listing. A draft that is closed is still
posted, so its evaluation is closed too.
=== patch src/bugflow/domain/polling.py
@@ -14,6 +14,7 @@ class PolledPullRequest(BaseModel):
     ref: PullRequestRef
     open: bool
+    draft: bool = False
     head_sha: str
     title: str
     body: str
=== patch src/bugflow/usecases/poll_pull_requests.py
@@ -71,6 +71,8 @@ class PollPullRequests:
             for pull in sorted(pulls, key=lambda p: p.updated_at):
+                if pull.draft and pull.open:
+                    continue
                 delivery = delivery_for(pull)
                 try:
                     outcome = self._ingress.send(delivery)
=== patch src/bugflow/adapters/github.py
@@ -88,6 +88,7 @@ def polled_pull_request_from_payload(
         ref=ref,
         open=payload["state"] == "open",
+        draft=bool(payload.get("draft")),
         head_sha=payload["head"]["sha"],
         title=payload["title"],
=== patch tests/unit/test_poll_pull_requests.py
@@ -168,3 +168,10 @@ def test_the_first_poll_asks_for_every_open_pull_request() -> None:
     assert feed.asked == [("o/r", None)]
     assert response.next_since == NOW - OVERLAP
+
+
+def test_an_open_draft_is_not_posted() -> None:
+    feed = FakeFeed({"o/r": [pull(7, draft=True), pull(8)]})
+    ingress = FakeIngress()
+    poll(feed, ingress, NOW - timedelta(hours=1))
+    assert [d.ref.number for d in ingress.received if d.ref] == [8]
