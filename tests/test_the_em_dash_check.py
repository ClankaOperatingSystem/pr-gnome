"""Run the em dash check over small documents, and check that it
reports the three dashes and no character that shares a byte with one.
The check runs in the C locale, where awk reads bytes.
"""

import os
import subprocess
import tempfile
from pathlib import Path

CHECK = (
    Path(__file__).resolve().parent.parent
    / "skills" / "pr-gnome-write" / "scripts" / "check-em-dash"
)


def findings(text: str) -> list[str]:
    with tempfile.TemporaryDirectory() as scratch:
        (Path(scratch) / "page.org").write_text(text)
        run = subprocess.run(
            [str(CHECK)],
            cwd=scratch,
            capture_output=True,
            text=True,
            check=False,
            env={**os.environ, "LC_ALL": "C"},
        )
    return [line for line in run.stdout.splitlines() if line]


def test_each_dash_is_reported() -> None:
    for dash in ("\u2014", "\u2013", "\u2015"):
        assert findings(f"Before {dash} after.\n"), dash


def test_arrows_minus_signs_and_quotation_marks_are_not_reported() -> None:
    text = "Order \u2192 delivery.\nIt runs at \u221218 degrees.\nSteps 1, 2, \u2026\nThe \u2018quoted\u2019 word.\n"
    assert findings(text) == []
