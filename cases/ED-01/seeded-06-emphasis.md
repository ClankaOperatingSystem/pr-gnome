title: Reject the previous secret after rotation
expect: VOICE-12
grade: warn
why: bold in running prose and an exclamation mark.
---
Once `WEBHOOK_SECRET_PREVIOUS` is emptied, deliveries signed with the old
secret are **never** accepted again!
