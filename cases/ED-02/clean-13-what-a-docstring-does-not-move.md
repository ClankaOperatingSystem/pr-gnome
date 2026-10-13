title: Say that the judge's fingerprint hashes its adapter
expect:
why: states what the docstring change does not move.
commit: Say that the judge's fingerprint hashes its adapter
|
| policy_source's docstring said the fingerprint follows the policy files
| and the code that renders them and nothing else, so that a retry fix no
| longer moves the corpus version. The fingerprint hashes the whole judge
| adapter beside them, retries included, and the docstring now says so.
|
| The probe-request fingerprint that would have made the old wording true
| is cancelled in cleanup.org (C1.18), with the reason: the churn it
| answered has mostly stopped since the restructure.
file: cleanup.org +11 -1
file: src/bugflow/method/adapters/policy_files.py +2 -4
---
Changing this docstring moves no fingerprint: `policy_files.py` is not among the sources the judge hashes, only its `unwrap` function is.
