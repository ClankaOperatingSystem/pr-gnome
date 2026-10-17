"""Run the commit message check over single messages and over a range
of a small repository, and check that it reports what GIT-3 forbids
and passes a plain message.
"""

import os
import subprocess
import tempfile
from pathlib import Path

CHECK = (
    Path(__file__).resolve().parent.parent
    / "skills" / "pr-gnome-write" / "scripts" / "check-commit-messages"
)


def check(message: str) -> tuple[int, list[str]]:
    run = subprocess.run(
        [str(CHECK), "-"], input=message, capture_output=True, text=True, check=False
    )
    return run.returncode, run.stdout.splitlines()


def test_a_plain_message_passes() -> None:
    assert check("Add the judge port\n\nThe judge had no way in.\n") == (0, [])


def test_a_subsystem_prefix_passes() -> None:
    assert check("cli: add the round trip command\n") == (0, [])


def test_a_summary_over_72_characters_is_reported() -> None:
    code, out = check("Add " + "a" * 70 + "\n")
    assert code == 1 and out == ["message: GIT-3 the summary is 74 characters, over 72"]


def test_a_character_of_several_bytes_counts_once() -> None:
    assert check("Add the café " + "a" * 59 + "\n") == (0, [])


def test_a_conventional_commit_prefix_is_reported() -> None:
    code, out = check("feat: add the judge port\n")
    assert code == 1 and "the prefix feat:" in out[0]


def test_a_first_word_that_is_not_imperative_is_reported() -> None:
    for summary in ("Added the port", "Adds the port", "Adding the port", "cli: added the port"):
        code, out = check(summary + "\n")
        assert code == 1 and "may not be imperative" in out[0], summary


def test_an_imperative_verb_with_the_ending_of_another_form_passes() -> None:
    for summary in ("Pass the port", "Focus the queue", "Address the gap",
                    "Bring the port", "Embed the font", "Proceed with the port"):
        assert check(summary + "\n") == (0, []), summary


def test_a_body_with_no_blank_line_is_reported() -> None:
    code, out = check("Add the port\nThe judge had no way in.\n")
    assert code == 1 and out == ["message: GIT-3 the second line is not blank"]


def test_a_body_line_over_72_characters_is_reported_and_a_long_url_is_not() -> None:
    code, out = check("Add the port\n\n" + "word " * 16 + "\n")
    assert code == 1 and out == ["message: GIT-3 line 3 is 80 characters, over 72"]
    url = "https://example.org/" + "a" * 80
    assert check(f"Add the port\n\n{url}\n") == (0, [])


def test_a_git_comment_line_is_not_read() -> None:
    assert check("Add the port\n\n# " + "x " * 50 + "\n") == (0, [])


def test_each_commit_of_a_range_is_read() -> None:
    env = {
        **os.environ,
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_CONFIG_SYSTEM": os.devnull,
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "test@example.org",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "test@example.org",
    }
    with tempfile.TemporaryDirectory() as scratch:
        def git(*args: str) -> str:
            return subprocess.run(
                ["git", *args], cwd=scratch, env=env, capture_output=True,
                text=True, check=True,
            ).stdout.strip()

        git("init", "-q", "-b", "master")
        git("commit", "-q", "--allow-empty", "-m", "Add the first commit")
        git("commit", "-q", "--allow-empty", "-m", "Added the second commit")
        git("commit", "-q", "--allow-empty", "-m", "Add the third commit")
        second = git("rev-parse", "--short", "HEAD~1")
        run = subprocess.run(
            [str(CHECK), "HEAD~2..HEAD"], cwd=scratch, env=env,
            capture_output=True, text=True, check=False,
        )
    assert run.returncode == 1
    assert run.stdout.splitlines() == [
        f"{second}: GIT-3 the summary may not be imperative: Added"
    ]
