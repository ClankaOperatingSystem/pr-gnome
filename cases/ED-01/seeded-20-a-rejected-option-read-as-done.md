title: Write the calibration-note test's note to copies
expect: VOICE-28
grade: warn
why: the opening words read as what the change did, and the last two words say it is what the change did not do.
---
Deleting the test was the alternative: `tests/unit/test_policy_files.py` holds the same property without writing. It stays because it proves the fingerprint unmoved by a note, where the unit test proves only that the note is left out of the source.
