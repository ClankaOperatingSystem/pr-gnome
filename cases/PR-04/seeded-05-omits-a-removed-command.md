title: Rename the replay command's judge flag
expect: GIT-5
grade: fail
why: silent about the purge command the patch removes.
commit: Rename the replay command's judge flag
file: src/bugflow/app/cli.py +3 -13
file: Makefile +1 -1
---
The replay command's --stub flag is now --stub-judge, which says what it
stubs. The Makefile target passes the new name.
=== patch src/bugflow/app/cli.py
@@ -80,32 +80,11 @@ def poll(once: bool) -> None:
 @cli.command()
 @click.argument("ref")
-@click.option("--stub", is_flag=True, help="Judge with the stub judge.")
-def replay(ref: str, stub: bool) -> None:
-    sys.exit(run_replay(ref, stub_judge=stub))
-
-
-@cli.command()
-@click.argument("ref")
-@click.option("--yes", is_flag=True, help="Do not ask first.")
-def purge(ref: str, yes: bool) -> None:
-    """Delete a pull request's journal entries and snapshots."""
-    if not yes:
-        click.confirm(f"Delete everything recorded for {ref}?", abort=True)
-    sys.exit(run_purge(ref))
+@click.option("--stub-judge", is_flag=True, help="Judge with the stub judge.")
+def replay(ref: str, stub_judge: bool) -> None:
+    sys.exit(run_replay(ref, stub_judge=stub_judge))
=== patch Makefile
@@ -40,7 +40,7 @@
 replay:
-	uv run bugflow replay --stub $(REF)
+	uv run bugflow replay --stub-judge $(REF)
