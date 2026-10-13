title: Bump temporalio to 1.33
expect: 
why: a dependency bump with its lock file.
commit: Bump temporalio to 1.33
file: pyproject.toml +1 -1
file: uv.lock +40 -40
---
temporalio 1.33 fixes the replay of workflows that continue as new while
a signal is pending. The lock file follows.
