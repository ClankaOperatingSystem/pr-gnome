title: Move the retry settings
expect: VOICE-32
grade: fail
why: "Its timeout" could be the timeout of the client or of the queue.
---
The client reads the queue on start, and this change moves its timeout into the settings file.
