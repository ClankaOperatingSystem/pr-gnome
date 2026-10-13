title: Revert "Cache the doctrine between evaluations"
expect: 
why: a revert is one reason.
commit: Revert "Cache the doctrine between evaluations"
file: src/bugflow/app/corpus.py +8 -46
file: tests/unit/test_corpus_version.py +0 -58
---
This reverts commit 7f2a91c. The cache held the doctrine past a change to
it, so an evaluation could run under a corpus version the files no longer
matched.
