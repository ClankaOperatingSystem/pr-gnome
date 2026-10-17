"""Run the attribution gate over single messages, as the commit-msg
hook does, and check that it fails on what ATTR-1 forbids and passes
a plain message.
"""

import subprocess
import tempfile
from pathlib import Path

GATE = Path(__file__).resolve().parent.parent / "tools" / "attribution-gate"


def gate(message: str) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as scratch:
        path = Path(scratch) / "COMMIT_EDITMSG"
        path.write_text(message)
        run = subprocess.run(
            [str(GATE), str(path)], capture_output=True, text=True, check=False
        )
    return run.returncode, run.stdout


def test_a_plain_message_passes() -> None:
    code, out = gate("Add a case for a phrase hung off the wrong noun\n\nThe judge passed it.\n")
    assert (code, out) == (0, "")


def test_a_co_authored_by_trailer_fails() -> None:
    code, out = gate("Fix the queue\n\nCo-Authored-By: Someone <someone@example.org>\n")
    assert code == 1 and ":3: " in out


def test_a_generated_with_line_fails() -> None:
    code, _ = gate("Fix the queue\n\nGenerated with a coding agent\n")
    assert code == 1


def test_a_session_trailer_or_url_fails() -> None:
    assert gate("Fix the queue\n\nAgent-Session: 4f3c2a19\n")[0] == 1
    assert gate("Fix the queue\n\nhttps://example.org/session/4f3c2a19\n")[0] == 1


def test_a_named_tool_fails() -> None:
    assert gate("Fix the queue as Codex suggested\n")[0] == 1


def test_a_git_comment_line_is_not_read() -> None:
    assert gate("Fix the queue\n# Co-Authored-By: a comment Git strips\n")[0] == 0
