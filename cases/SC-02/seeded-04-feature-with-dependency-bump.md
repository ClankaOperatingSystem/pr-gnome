title: Add the Forgejo delivery adapter
expect: GIT-4
grade: fail
why: a feature and a dependency upgrade in one commit.
commit: Add the Forgejo delivery adapter and upgrade httpx2
file: src/bugflow/adapters/forgejo_delivery.py +180 -0
file: tests/unit/test_forgejo_delivery.py +120 -0
file: pyproject.toml +1 -1
file: uv.lock +240 -180
---
Forgejo's webhook payloads are normalised to the same delivery the GitHub
adapter produces, so everything downstream of the ingress is the same on
both forges. httpx2 goes from 0.9.2 to 0.11.0 in the same commit.
