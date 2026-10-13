title: Revert the rename of the evaluate command
expect: 
why: "Revert" is judged alone, and it is imperative.
commit: Revert "Rename the evaluate command to assess"
---
The rename broke the Makefile targets that call evaluate.
