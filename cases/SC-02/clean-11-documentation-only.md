title: Record the first dismissal on a real pull request
expect: 
why: a commit of documentation only.
commit: Record the first dismissal on a real pull request
file: index.org +34 -2
---
A reviewer dismissed SC-01 on pull request 62 with a reason, the worker
recorded it, and the label went back to `doctrine:pass` on the next
evaluation. What the journal holds for that dismissal is written down where
the dismissal design is, because until now nothing had exercised it outside
the tests.
