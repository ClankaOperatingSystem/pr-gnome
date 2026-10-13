# The narrative doctrine

Standards for written work: commit messages, pull request descriptions,
comments and documents. A doctrine of clauses, a policy for each
judgement, cases that test the judge, one check that needs no model, and
a skill that writes to the doctrine.

Two things read this repository and nothing in it is written for one
alone:

- **A bugflow server** judges pull requests by it when a binding
  repository deploys it, with `declarations.toml` saying which
  repositories it applies to. bugflow's `docs/policy-package.md` says
  what the server reads.

- **A garden node** declares it as a methodology, beneath its
  methodologies path, at a directory named `narrative`:

      children:
        - path: methodologies/narrative
          remote: git@github.com:ClankaOperatingSystem/narrative-doctrine.git

  The node's tree tool links `skills/narrative-write` into its skills and
  the check in `bin/` into its commands, and its lint runs the check that
  `methodology.yaml` names. poslib's `doc/pos-methodology.txt` says how.

## What is here

| Path | What it is |
|---|---|
| `doctrine/*.md` | The doctrine, read in filename order as one document |
| `policies/<ID>-<name>.md` | One policy each: header, instructions, calibration notes |
| `cases/<ID>/*.md` | The cases of policy `<ID>`: an example pull request and the answer a correct judge gives |
| `cases/README.md` | Where the older cases came from, and what their names mean |
| `manifest.md` | The product's id, subjects, policies and checks |
| `bin/narrative-em-dash` | The check that answers ED-04 without a model |
| `lib/` | What the check uses |
| `skills/narrative-write/` | The skill that drafts and checks prose against the doctrine |
| `methodology.yaml` | The declaration a garden's lint reads: the check to run |
| `tests/` | The checks that every file is in the format the consumers read |

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

## The format of a policy file

A header, a line of three dashes, the instructions, a line
`=== calibration`, and the calibration notes. The header lines:

- `policy_id`: the policy's id. The filename opens with it.
- `subject`: what the policy judges, in two or three words.
- `summary`: one sentence that says what a compliant pull request does.
- `model_class`: `small`, `medium` or `large`.
- `evidence`: the part of the pull request the model is shown:
  `description`, `commits`, `scope` or `patches`.
- `quotable_name`: the name of the text a finding may quote from.
- `graded`: `yes` when the model is asked a grade for each finding.
- `quotes_code`: `yes` when a quote may come from a patch.
- `ceiling`: the worst grade a finding may carry; absent, `fail`.
- `clause`: one clause the policy judges, its id and name. It repeats.

## The format of a case

A header, a line of three dashes, and the description of the example
pull request:

    title: Retry the judge on a timeout
    expect: GIT-4
    grade: fail
    why: The body names a second change with a reason of its own.
    commit: Retry the judge on a timeout
    |
    | Also renames the poller's settings.
    file: src/judge.py +12 -3
    ---
    Retries the judge once when the model does not answer in time.
    === patch src/judge.py
    @@ -40,3 +40,12 @@

`expect` is the clause a correct judge reports, empty in a clean case;
`grade` the grade it gives; `why` the reason, which the judge is not
shown; `commit` one commit's summary with the lines after it that open
with `|` the rest of its message; `file` one changed file's path and line
counts; `=== patch <path>` the patch of a file the header lists.

## Checks

    uv run --with pytest pytest -q

checks every file against the formats. `bin/narrative-em-dash` runs in
any directory, reads its Org and Markdown files, and prints findings as
`FILE:LINE: MESSAGE`, exit 1 when there are any.
