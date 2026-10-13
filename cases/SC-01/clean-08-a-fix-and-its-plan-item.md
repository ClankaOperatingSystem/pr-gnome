title: Declare deploy-check phony
expect:
why: the plan item is part of the change that closes it.
commit: Declare deploy-check phony
|
| Every other target in the Makefile is in .PHONY and deploy-check was
| not, so a file of that name in the repository root would stop make
| running it.
|
| Closes C1.17 in cleanup.org.
file: Makefile +1 -1
file: cleanup.org +1 -1
file: index.org +1 -1
---
The target is declared phony, and the plan item that records it is marked done.
