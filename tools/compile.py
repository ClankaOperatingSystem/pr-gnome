"""Copy the doctrine and the policies into each skill.

The doctrine and the policies are written once, in doctrine/ and
policies/ at the root. The skills command-line tool copies a skill's
directory and nothing outside it, so each skill in skills/ gets a copy
of both under its references/ directory, with a README saying where the
source is.

    python3 tools/compile.py [OUTPUT]

writes the copies into OUTPUT/skills/<name>/references/, OUTPUT being
the root of this repository when it is not given. The format tests give
a scratch directory, and compare what is written there with what is
committed.
"""

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ("doctrine", "policies")
NOTE = """\
# Generated: do not edit

The directories beside this file are copies of `doctrine/` and
`policies/` at the root of the pr-gnome repository, written by
`make skills`. Edit the files at the root and run `make skills`; a
change made here is lost, and `make check` reports it.
"""


def compile_skills(output: Path) -> list[Path]:
    """Write each skill's references/ under output, and return the
    directories written."""
    written = []
    for skill in sorted((ROOT / "skills").glob("*/")):
        if not (skill / "SKILL.md").is_file():
            continue
        references = output / "skills" / skill.name / "references"
        if references.exists():
            shutil.rmtree(references)
        references.mkdir(parents=True)
        for name in SOURCES:
            source = ROOT / name
            if any(source.glob("*.md")):
                shutil.copytree(source, references / name)
        (references / "README.md").write_text(NOTE)
        written.append(references)
    return written


if __name__ == "__main__":
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    for references in compile_skills(output):
        print(references)
