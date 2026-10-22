# pr-gnome

Standards for written work: commit messages, pull request descriptions,
comments and documents. A doctrine of clauses, a policy for each
judgement, cases that test the judge, one check that needs no model, and
a skill that writes to the doctrine.

This repository is a gnome: a methodology that also holds a doctrine,
its policies and its cases. bugflow's
[What a gnome is](https://github.com/bugflow/bugflow/blob/master/docs/gnomes.md)
defines a gnome and a maintainer's tasks, its
[policy package](https://github.com/bugflow/bugflow/blob/master/docs/policy-package.md)
specifies each file, and its
[words](https://github.com/bugflow/bugflow/blob/master/docs/words.md)
give each term one line.

Two things read this repository and nothing in it is written for one
alone:

- **A bugflow server** judges pull requests by it when a binding
  deploys it. bugflow's
  [review document](https://github.com/bugflow/bugflow/blob/master/docs/review.md)
  says what a review writes and where each part comes from.

- **A garden** declares it as a methodology in its configuration, at a
  tag, as ClankOS's `clankos-run help install` says:

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

`doctrine/` and `policies/` are the originals. After a change in
either, run `make skills`, which writes the skill's copy in its
`references/`; the tests fail if the copy is out of date.

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
to `master`. `scripts/check-em-dash` reads the files it is given, or the
text on standard input with `-`, or with neither the Org and Markdown
files of the directory it runs in, and prints findings as
`FILE:LINE: MESSAGE`, exit 1 when there are any. `scripts/check-commit-messages` reads the
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
