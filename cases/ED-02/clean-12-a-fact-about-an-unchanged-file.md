title: Fire the quarterly cadence four times a year
expect:
why: states a fact about a file the change does not touch.
commit: Fire the quarterly cadence four times a year
|
| The quarterly calendar was the first of January only, the same as the
| annual one, so a quarterly layer would have taken stock once a year. It
| fires on the first of January, April, July and October.
|
| Closes C1.5 in cleanup.org.
file: cleanup.org +1 -1
file: src/bugflow/app/schedules.py +6 -4
file: tests/unit/test_what_a_cadence_schedules.py +8 -0
---
No layer in `reviewers/pace-layers.toml` uses the quarterly cadence yet, so no schedule changes on deploy. A quarterly layer added later gets the right calendar.
