title: Count dropped retries against the quota
expect:
why: the clause keeps its "that", so "retries the judge" is never formed.
---
The retries that the judge drops now count against the quota. Before this
change only a retry that reached the model was counted, so a run of
timeouts spent nothing and was never stopped.
