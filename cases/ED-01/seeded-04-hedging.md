title: Retry refused deliveries
expect: VOICE-10
grade: warn
why: "It's worth noting" and "arguably" hedge a claim that is neither made nor stated as open.
---
The poller keeps its time window when the ingress refuses a delivery, so the
next poll posts it again.

It's worth noting that the ingress could arguably queue refused deliveries
itself.
