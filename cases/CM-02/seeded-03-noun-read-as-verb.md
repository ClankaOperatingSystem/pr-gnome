title: Stop the poller sending an update twice
expect: VOICE-28
grade: warn
why: "updates" has no article, so "updates the poller" is formed first.
commit: Drop updates the poller sends twice
---
The poller sent an update again when its acknowledgement was late.
