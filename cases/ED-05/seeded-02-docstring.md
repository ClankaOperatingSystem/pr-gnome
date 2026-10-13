title: Read the stale records from the journal
expect: VOICE-28
grade: warn
why: "Return records" is formed first, because "records" has no article and the clause no "that".
commit: Read the stale records from the journal
file: src/journal/reader.py +4 -0
---
The sweep needs the records the journal has marked stale.
=== patch src/journal/reader.py
@@ -88,3 +88,7 @@ class Reader:
         return self._rows
+
+    def stale(self) -> list[Record]:
+        """Return records the journal marks stale."""
+        return [row for row in self._rows if row.stale]
