title: Close pull request workflows when the poller sees a close
expect: 
why: an open question stated with what would settle it is not hedging.
---
The poller posts `closed` for a pull request closed since its last poll, and
the pull request's workflow ends.

Not settled: whether a pull request reopened with nothing changed should be
evaluated again. Deciding it needs the forge's reopened event, which the
pull request listing does not report.
