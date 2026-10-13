title: Run the parser's tests on empty input
expect:
why: the clause keeps its "that", so "tests" is never read as a verb.
commit: Fix the tests that the new parser breaks on empty input
---
The parser's tests now pass on an empty file.
