title: Prepare the journal for the warehouse
expect: 
why: three commits that are each one reason.
commit: Reject updates to the journal with a trigger
commit: Record the corpus version on every finding
commit: Index the journal by repository and pull request
file: migrations/versions/0003_journal_append_only.py +48 -0
file: migrations/versions/0004_corpus_version.py +22 -0
file: migrations/versions/0005_journal_indexes.py +18 -0
file: src/bugflow/adapters/sqlalchemy_journal.py +40 -12
file: tests/integration/test_journal_contract.py +96 -0
---
Three steps toward the published contract the warehouse reads. Each is its
own migration and its own commit: the append-only trigger, the corpus
version on findings, and the indexes the warehouse's queries need.
