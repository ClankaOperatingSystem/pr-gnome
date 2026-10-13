title: Declare deploy-check phony
expect: VOICE-15
grade: fail
why: "L6.9" stands in for the thing it names.
---
A doctrine test holding every Makefile target to `.PHONY` is proposed in the learning loop (L6.9), which would have caught this.
