title: Clean up the ingress
expect: GIT-4
grade: fail
why: "Clean up the ingress" names a group and no change.
commit: Clean up the ingress
file: src/bugflow/app/ingress.py +86 -54
file: src/bugflow/adapters/webhook_sink.py +24 -18
file: src/bugflow/usecases/receive_delivery.py +40 -22
file: tests/unit/test_webhook_ingress.py +96 -40
file: .env.example +4 -2
file: docker-compose.yml +6 -2
---
The ingress has needed attention for a while. Signature verification is
tidier, the sink no longer swallows errors, the delivery id is logged, the
health check returns a body, and two settings that were never read are gone.
