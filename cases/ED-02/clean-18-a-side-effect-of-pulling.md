title: Untrack the coverage database
expect:
why: states a side effect of pulling the change.
commit: Untrack the coverage database
|
| .coverage, a 53 KB database, was committed with an unrelated change,
| and nothing in the repository measures coverage. It is removed from
| the index and ignored.
|
| Closes C1.10 in cleanup.org.
file: .coverage +0 -0
file: .gitignore +1 -0
file: cleanup.org +1 -1
file: index.org +1 -0
---
Pulling this deletes a local `.coverage`, since git removes a tracked file that another commit untracks. The next coverage run writes it again, ignored.
