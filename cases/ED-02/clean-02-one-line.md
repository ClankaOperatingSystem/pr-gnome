title: Bump httpx2 to 0.4.1
expect: 
why: one line that states the problem.
commit: Bump httpx2 to 0.4.1
file: pyproject.toml +1 -1
file: uv.lock +41 -39
---
0.4.0 leaked a connection whenever a request timed out, which the worker does whenever the judge is slow.
