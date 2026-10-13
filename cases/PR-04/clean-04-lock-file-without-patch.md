title: Bump httpx2 to 0.4.1
expect: 
why: a lock file with no patch moves with the bump, as the description says.
commit: Bump httpx2 to 0.4.1
file: pyproject.toml +1 -1
file: uv.lock +41 -39
---
httpx2 0.4.0 leaked a connection when a request timed out, which the worker
does whenever the judge is slow. 0.4.1 fixes it. The lock file moves with the
bump.
=== patch pyproject.toml
@@ -12,7 +12,7 @@ dependencies = [
     "alembic>=1.13",
-    "httpx2>=0.4.0",
+    "httpx2>=0.4.1",
     "pydantic>=2.7",
