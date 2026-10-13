title: Move signing into its own module
expect: VOICE-2
grade: fail
why: a paragraph that lists the changed files.
commit: Move signing into its own module
file: src/bugflow/adapters/signing.py +8 -0
file: src/bugflow/adapters/webhook_sink.py +2 -10
file: tests/unit/test_webhook_sink.py +1 -1
---
Signing moves out of the webhook sink.

Files changed: adapters/signing.py, adapters/webhook_sink.py and tests/unit/test_webhook_sink.py. Three files in total, two under adapters and one under tests.
