title: Scan for credentials in make check and CI
expect: 
why: the timing says who measured it, so it is not fake precision.
---
The scan runs gitleaks 8.30.1 over the commits since `origin/master`, the
staged changes and the unstaged changes.

Scanning the repository's full history of 65 commits took 0.7 seconds on this
laptop, as reported by gitleaks itself.
