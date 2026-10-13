title: Retry on a timeout
expect: GIT-3
grade: warn
why: "should retry" describes what ought to happen; conjugating it recovers the instruction.
commit: The judge should retry on a timeout
---
A timed-out request is now retried. The summary describes what ought to happen rather than instructing the code.
