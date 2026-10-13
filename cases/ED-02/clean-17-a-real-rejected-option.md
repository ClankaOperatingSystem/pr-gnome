title: Write the calibration-note test's note to copies
expect:
why: a rejected option with its reason.
commit: Write the calibration-note test's note to copies
|
| A doctrine test appended to CM-01's shipped policy file and restored it
| in a finally, so an interrupted run left reviewers/ edited for every
| session sharing the tree. It copies the policy files to a temporary
| directory and writes there; policy_source already takes a directory.
|
| Closes C1.9 in cleanup.org.
file: cleanup.org +5 -1
file: tests/doctrine/test_the_corpus_is_one_list.py +18 -13
---
The alternative was to delete the test: `tests/unit/test_policy_files.py` holds the same property without writing. It stays because it proves the fingerprint unmoved by a note, where the unit test proves only that the note is left out of the source.
