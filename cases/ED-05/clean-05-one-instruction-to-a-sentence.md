title: Reword the useful description policy's summary
expect:
why: each sentence gives one instruction, with a literal verb and a named object.
commit: Reword the useful description policy's summary
file: narrative/policies/ED-02-useful-description.md +1 -1
---
The summary line is the heading an author is shown above a finding.
=== patch narrative/policies/ED-02-useful-description.md
@@ -1,5 +1,5 @@
 policy_id: ED-02
 subject: description
-summary: The description carries what the diff cannot show, and no more
+summary: The description should state what is not obvious from the diff. Do not simply describe the diff
 model_class: medium
