title: Add the warehouse export
expect: GIT-4
grade: warn
why: a subsystem of five parts that could have arrived in steps.
commit: Add the warehouse export
file: src/bugflow/usecases/export_journal.py +340 -0
file: src/bugflow/adapters/parquet_export.py +280 -0
file: src/bugflow/adapters/s3_sink.py +190 -0
file: src/bugflow/ports/export.py +70 -0
file: src/bugflow/app/cli.py +120 -2
file: tests/unit/test_export_journal.py +420 -0
file: tests/integration/test_parquet_export.py +210 -0
---
The journal is exported to Parquet and written to object storage on a
schedule, partitioned by day, with the schema the bronze layer reads. The
export, both adapters, the port, the command and the tests arrive together.
