title: Close the stocktake early-journal item
expect:
why: states a fact about a row the fix leaves as it is.
commit: Close the stocktake early-journal item
|
| C1.16 in cleanup.org, a stocktake journalling its run on the first
| poll, was fixed by 774b387, which gave a run still going an outcome of
| its own. The item is marked done with that commit named, and the
| signal-based wait stays with its todo.org item.
file: cleanup.org +7 -1
---
The row written before the fix, for the first range review, still records a run collected mid-way; the journal is append-only, so it stays.
