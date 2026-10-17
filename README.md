# pr-gnome

Standards for written work: commit messages, pull request descriptions,
comments and documents. A doctrine of clauses, a policy for each
judgement, cases that test the judge, one check that needs no model, and
a skill that writes to the doctrine.

This repository is a gnome: it implements the gnome protocol, which
bugflow's [policy package](https://github.com/bugflow/bugflow/blob/master/docs/policy-package.md) specifies.
[What a gnome is](https://github.com/bugflow/bugflow/blob/master/docs/gnomes.md) explains a gnome's parts, who reads each,
and a maintainer's tasks.

Two things read this repository and nothing in it is written for one
alone:

- **A bugflow server** judges pull requests by it when a binding
  repository deploys it, with `declarations.toml` saying which
  repositories it applies to.

- **A garden** declares it as a methodology in its configuration, at a
  tag:

      methodologies:
        - source: https://github.com/ClankaOperatingSystem/pr-gnome.git
          ref: TAG

  The skills command-line tool copies `skills/pr-gnome-write/` into the
  garden's skills, and the garden's lint runs the check in its
  `scripts/`.

## What is here

| Path | What it is |
|---|---|
| `doctrine/*.md` | The doctrine, read in filename order as one document |
| `policies/<ID>-<name>.md` | One policy each: header, instructions, calibration notes |
| `skills/pr-gnome-write/` | The skill that drafts and checks prose against the doctrine |
| `skills/pr-gnome-write/references/` | A copy of `doctrine/` and `policies/`, written by `make skills` |
| `skills/pr-gnome-write/scripts/check-em-dash` | The check that answers ED-04 without a model |
| `skills/pr-gnome-write/scripts/check-commit-messages` | The check of the commit message rules of GIT-3 that need no model |
| `skills/pr-gnome-write/scripts/lib/` | What the checks use |
| `cases/<ID>/*.md` | The cases of policy `<ID>`: an example pull request and the answer a correct judge gives |
| `cases/README.md` | Where the older cases came from, and what their names mean |
| `manifest.md` | The gnome's id, subjects, policies and checks |
| `tools/compile.py` | What `make skills` runs |
| `tools/attribution-gate`, `.githooks/commit-msg` | The gate that fails a commit message carrying AI attribution |
| `tests/` | The checks that every file is in the format the consumers read |

The doctrine and the policies are kept in `doctrine/` and `policies/`.
The skills command-line tool copies a skill's directory and nothing
outside it, so the skill carries a copy of both in its `references/`.
After a change in `doctrine/` or `policies/`, run `make skills`. The
tests fail if the copy is out of date.

## Words

- Doctrine: the standard, in `doctrine/`, joined in filename order.
- Clause: one rule of the doctrine, with an id such as `VOICE-6`. An id
  is never reused.
- Policy: one question asked about a pull request, and the clauses it
  judges. ED-04 is a check and has no file.
- Subject: the evidence a policy reads: `pull-request/description`,
  `pull-request/commits`, `pull-request/scope` or `pull-request/patches`.
  A policy file names the kind alone, `description`, as the server reads
  it.
- Case: an example pull request with the answer a correct judge gives
  it. A `clean` case expects nothing; a `seeded` case expects one clause.
- Finding: one thing a judge or a check reports, quoting the words at
  fault and citing a clause, graded `warn` or `fail`.
- Calibration: one run of a policy over all of its cases. The command is
  a server's; the figures go in the policy's calibration notes.

## The formats

The [policy package](https://github.com/bugflow/bugflow/blob/master/docs/policy-package.md) specifies the manifest, a policy file
and a case. The tests here check every file against it.

## Adding a case

A case is one example pull request and the answer a correct judge
gives it. The policy package specifies the header and the body. In
this repository:

- Put it in `cases/<ID>/`, the directory of the policy it tests, named
  `clean-NN-name.md` or `seeded-NN-name.md`, where `NN` is the next
  number in that directory.
- In a seeded case, give `expect` one clause that the policy's header
  lists, and `grade` the grade a correct judge gives. In a clean case,
  leave `expect` empty.
- Say in `why`, in one sentence, what makes the case clean or seeded.
  The judge is not shown it.
- Use invented names for people, files and records.
- Add a dated line to the policy's calibration notes saying what was
  added and that it is not measured.

`make check` checks the new file against the format.

## Checks

    uv run --with pytest pytest -q

checks every file against the formats. `make check` runs the same
command, and GitHub Actions runs it on each pull request and each push
to `master`. `scripts/check-em-dash` runs in any directory, reads its
Org and Markdown files, and prints findings as `FILE:LINE: MESSAGE`,
exit 1 when there are any. `scripts/check-commit-messages` reads the
messages of the commits in `origin/master..HEAD`, or of a range it is
given, or one message on standard input with `-`, and prints findings
as `COMMIT: GIT-3 MESSAGE`.

## The attribution gate

ATTR-2 of the doctrine has each repository enforce ATTR-1 with a gate
of its own, on the client and in CI. Here it is `tools/attribution-gate`,
which fails when a commit message carries a `Co-Authored-By` trailer, a
"Generated with" line, a session trailer or URL, or the name of a
coding agent; the names are listed in the script. Once per clone,

    make hooks

points Git's hooks at `.githooks/`, whose `commit-msg` hook runs the
gate on each message. GitHub Actions runs it over the commits of each
pull request.

## Website

[Read the current standards](https://clankaoperatingsystem.github.io/pr-gnome/).
The site includes worked examples and paths for contributors, maintainers and
people assessing the standards. Its reader guidance is in `site.toml`.

`requirements-site.txt` pins the renderer release and its wheel checksum.
To build locally, install that file and run this from a clean checkout:

```sh
python -m pip install -r requirements-site.txt
gnome-site . _site --title pr-gnome \
  --repository https://github.com/ClankaOperatingSystem/pr-gnome \
  --revision "$(git rev-parse HEAD)" --content site.toml
```

The output directory must be new or empty. The Website workflow runs the source
checks and builds a downloadable `pr-gnome-site` artifact for each pull request.
Download and extract that artifact, then open `index.html` to review it.
Changes on `master` replace the current GitHub Pages site after the checks pass.
The repository's Pages publishing source is GitHub Actions.

The gnome's maintainers own `site.toml`, the renderer pin and the workflow.
Review the preview when changing standards or upgrading the renderer. Source
links identify the rendered commit; policy routes and clause anchors stay stable.

## Licence

This repository is free software under the GNU General Public License,
version 3 or any later version. The text is in `COPYING`.
