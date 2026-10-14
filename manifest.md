agent_id: narrative
summary: What a change says about itself: its description, its commits, its scope
subjects: pull-request/description, pull-request/commits, pull-request/scope, pull-request/patches
policies: CM-01, CM-02, ED-01, ED-02, ED-03, ED-04, ED-05, PR-04, SC-01, SC-02
checks: em-dash ED-04 VOICE-21
---

This file describes the gnome to whatever reads it. The lines above
the three dashes are read by a bugflow server and by the format tests;
the text below is for a person.

The narrative reviewer reads what a pull request says about itself: its
title, its description, its commit messages and the list of files it
changes. It does not review code for correctness. Two policies are also
shown the patches: PR-04 compares the description with them, and ED-05
reads the comments and docstrings they add.

- `agent_id` is the reviewer's id on a server. The commit status on a
  pull request has this name.
- `summary` is one line saying what the policies read.
- `subjects` lists the kinds of evidence the policies ask for.
- `policies` lists every policy. A policy judges a repository on a server
  only when the server's declarations also list it for that repository.
- `checks` names a check that a server performs in code: the check's name,
  the policy it answers and the clause its findings cite. ED-04, the em
  dash check, has no policy file; in a garden the script
  `skills/pr-gnome-write/scripts/check-em-dash` answers it under the lint.
