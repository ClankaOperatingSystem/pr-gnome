title: Keep the poll window after a failure
expect: VOICE-11
grade: warn
why: "So what happens when" is a question used as a transition.
---
So what happens when the ingress is down? The poller keeps its time window
and posts the same deliveries on the next poll.
