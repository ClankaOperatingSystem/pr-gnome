title: Retire the deterministic policies
expect: 
why: "ADR-013" is repeated because it is being cited, after the record is named.
commit: Retire the deterministic policies from the corpus
file: src/bugflow/policy/deterministic.py +0 -266
---
The decision record "The reviewbot judges; tools check" (ADR-013) says that a mechanical check belongs to the tool that can make it. Under ADR-013 these eight are retired: a hook or a linter decides them, and every repository runs those already.
