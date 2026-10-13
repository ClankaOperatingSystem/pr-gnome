title: Load the fixtures before the migration runs
expect: VOICE-28
grade: fail
why: "Test fixtures load" has two complete readings, and nothing in the sentence chooses one.
commit: Test fixtures load before the migration
---
The migration read a table the fixtures had not yet filled.
