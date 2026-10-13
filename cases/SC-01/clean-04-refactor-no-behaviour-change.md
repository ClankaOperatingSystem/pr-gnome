title: Share the judge's completion and report parsing
expect: 
why: a refactor with one purpose and no behaviour change.
commit: Share the judge's completion and report parsing
file: src/bugflow/adapters/litellm_judge.py +60 -48
---
assess and reproduce each posted a chat completion and parsed its report.
Both now call the same two helpers, with the same errors as before.
