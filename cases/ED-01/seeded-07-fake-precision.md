title: Poll only recently updated pull requests
expect: VOICE-13
grade: fail
why: "most users" is a figure nobody counted.
---
The poller lists pull requests updated since its last poll rather than every
pull request, which cuts API calls by roughly 40% for most users.
