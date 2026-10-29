# Git and pull requests

**GIT-1. Feature branches.** Never commit to the default branch. Every change goes on a
feature branch and through a pull request, single-line changes and
documentation-only changes included.

**GIT-2. Branch names.** Branch names are plain and descriptive: `agents-doctrine`,
`journal-migrations`. No `feat/`, `fix/`, `chore/` prefixes.

**GIT-3. Commit messages.** Commit messages are kernel style:

- Imperative mood. "Add the judge port", not "Added" or "Adds".
- A summary line that is a directive, 50 characters or fewer where it can be
  without losing the point, 72 at the outside.
- A blank line, then a body that says what was wrong and why this change is
  the right response. Wrap at 72.
- No conventional-commit prefixes (`feat:`, `fix:`, `chore:`). A subsystem
  prefix is different and welcome: `cli: add the round trip command` names
  the code the change touches, where `feat:` names a category of change and
  says nothing.
- The summary says what the change does, not what it is not. "Make the round
  trip a command, not only a test" spends half a line on the old state;
  "cli: add the round trip command" is the same change in fewer words.

**GIT-4. One reason.** Each commit (and pull request) should exist for a
single reason. The reviewer needs to understand quickly what changed and
why. Divide the work into changes that each make sense alone.

Size is not the test. A rule that is applied mechanically across a thousand files
is one reason, because every edit in it is the same edit and splitting it would
divide a set rather than separate two ideas. A minimal fix to one problem is
one reason at six hundred lines, because its parts do not stand alone: the
intermediate states would not build or would not make sense.

What is forbidden is two reasons in one change. Two unrelated things that
could each have been committed, reviewed and reverted on their own belong in
two commits. The sign is that each half is a change someone could describe. A body that needs the word "also" is another sign, and a body without the
word proves nothing. A summary that names a group of changes, such as "fix
the ugly parts of the parser" or "various cleanups", has the same fault.

Related work can also be too much. A change whose parts genuinely belong
together, but which no one reviewer can reason about as a whole, is split
into a sequence that can be followed, each step standing on its own. Where it
cannot be split without breaking, the message says why it is indivisible.

**GIT-5. Pull request descriptions.** The pull request description states the problem, the change, and
anything a reviewer would otherwise have to reverse-engineer from the diff.
It matches the diff: it does not describe work that is not there, and
it does not omit work that is.

A description runs to 200 words at most, outside code blocks. A reviewer
who must read more before the diff reads less of it. What a longer
description would hold belongs in the commit bodies, or in the documents
the change edits.

**GIT-6. No way round a gate.** Never use `--no-verify`, `--force` against a shared branch, or any
other route around a gate. A gate that is wrong is fixed in its own pull
request.
