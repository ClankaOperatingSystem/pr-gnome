title: Run the parser's tests on empty input
expect: VOICE-28
grade: warn
why: one garden path among two plain summaries.
commit: Add an empty fixture
commit: Fix tests the new parser breaks on empty input
commit: Document the fixture
---
The parser's tests now pass on an empty file.
