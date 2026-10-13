title: Publish internal stack ports on 127.0.0.1 only
expect: 
why: a configuration change with the documentation and the test it needs.
commit: Publish internal stack ports on 127.0.0.1 only
file: docker-compose.yml +3 -3
file: .env.example +6 -4
file: index.org +12 -6
file: tests/doctrine/test_published_ports_are_local.py +55 -0
---
Postgres, Temporal and its UI published their ports on every interface.
They now publish on 127.0.0.1, with a test that keeps them there.
