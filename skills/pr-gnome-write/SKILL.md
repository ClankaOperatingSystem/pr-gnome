---
name: pr-gnome-write
description: Draft and check prose against the pr-gnome doctrine before it goes out. Load before writing any commit message, pull request description, decision record, task entry, docstring or reply in a repository that installs this skill.
---

# Write to the doctrine

The doctrine is in `references/doctrine/`, beside this file, and its
policies are in `references/policies/`. Read the doctrine at the start
of the session, before the first piece of prose, so the clauses in force
are the current ones. Do not work from memory of them.

Then, for every piece of prose, draft it and apply each policy in
`references/policies/` to the draft as the policy's instructions say, before it is
sent. Each policy is a rewrite, not a glance:

1. ED-01, the editorial voice: no marketing register, filler, hedging,
   padding or narrating yourself; name what a reference refers to; give a
   noun its article and keep "that" before a clause.
2. ED-02, a useful description: say what the diff cannot, and never
   restate a commit body.
3. ED-03, model tics: no triples where one fact is meant, no closing
   maxims, no "X, not Y" tails with no live alternative, no bold in
   running prose.
4. CM-01 and CM-02, commit summaries: imperative mood, one change, read
   the opening words alone for a phrase the summary does not mean.
5. SC-01 and SC-02, scope: one reason per commit and per pull request.
6. PR-04, honesty: the description claims nothing the patches do not
   show.
7. ED-04: no em dashes; `scripts/check-em-dash` finds them.

Then strike each sentence in turn. If no fact leaves with it, it stays
struck.

Write in the active voice. Do not write who decided or approved a change,
or when: it is not what the change is. Never present a proposal of your
own as the maintainer's decision.
