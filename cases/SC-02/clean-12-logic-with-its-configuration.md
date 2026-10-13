title: Take the poll interval from the environment
expect: 
why: logic with the configuration and documentation it needs.
commit: Take the poll interval from the environment
file: src/bugflow/app/poller.py +12 -3
file: tests/unit/test_poller_settings.py +38 -0
file: .env.example +4 -0
file: docker-compose.yml +2 -0
---
The poller's interval was hard coded at thirty seconds, which is too often
for a laptop and too seldom for the stack. It now reads POLL_INTERVAL, which
the compose file passes and the example environment documents.
