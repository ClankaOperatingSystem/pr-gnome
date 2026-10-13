title: Accept the previous webhook secret while rotating
expect: 
why: a bold label that opens a paragraph is a heading, not emphasis.
---
**Problem.** Changing `WEBHOOK_SECRET` rejected every delivery the forge
signed with the old secret until its webhook configuration caught up.

**Change.** The ingress also reads `WEBHOOK_SECRET_PREVIOUS`. A delivery
signed with it is accepted and logged with its delivery id. An empty previous
secret accepts nothing.

**Verification.** Five new unit tests, and a live run against the ingress:
the old secret got 202 while rotating and 401 afterwards.
