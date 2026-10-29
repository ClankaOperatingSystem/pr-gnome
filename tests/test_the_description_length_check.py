"""Run the description length check over small descriptions, and check
that it counts the words outside code blocks against the limit of
GIT-5.
"""

import subprocess
from pathlib import Path

CHECK = (
    Path(__file__).resolve().parent.parent
    / "skills" / "pr-gnome-write" / "scripts" / "check-description-length"
)


def run(text: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(CHECK), "-"], input=text, capture_output=True, text=True, check=False
    )


def test_a_description_of_200_words_passes() -> None:
    assert run("word " * 200).returncode == 0


def test_a_description_over_200_words_is_reported() -> None:
    result = run("word " * 201)
    assert result.returncode == 1
    assert result.stdout.splitlines() == ["-: GIT-5 description runs to 201 words, over 200"]


def test_the_words_of_a_code_block_are_not_counted() -> None:
    assert run("word " * 150 + "\n```\n" + "output " * 100 + "\n```\n").returncode == 0


def test_with_no_description_it_could_not_check() -> None:
    assert subprocess.run([str(CHECK)], capture_output=True, check=False).returncode == 2
