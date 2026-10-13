title: Publish the summary comment as the owner
expect: 
why: states a risk that the diff cannot show.
commit: Publish the summary comment as the owner
file: src/bugflow/usecases/publish_findings.py +30 -4
---
Publishing posts as whoever owns the token, so every comment this makes is attributable to the owner personally. That is the risk being accepted while there is one posting identity; several identities, one per aspect of quality, are the intended end state.
