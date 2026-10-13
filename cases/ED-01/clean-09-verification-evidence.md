title: Poll pull requests into the ingress
expect:
why: what was run and what the system did is evidence, not narrating.
---
The poller lists this repository's pull requests and posts each change to the
ingress as a signed `pull_request` delivery.

**Verification.**
- A poll from the host posted this pull request as `synchronize`, and the
  ingress started its workflow.
- A second poll posted it again, and the ingress answered `duplicate`.
- A push and an edit to the description reached the ingress as one delivery,
  and the summary comment was edited in place.
