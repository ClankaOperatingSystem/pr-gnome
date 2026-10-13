"""Check every file of the product against the formats the server
and the calibration command read, before a pull request is opened.

The server checks a deployment when a pull request is opened, but it
reads only the policies, the doctrine and the manifest. Nothing else reads the cases until a calibration runs. This
file checks all of them, in the terms README.md gives under "The format
of a policy file" and "The format of a case".
"""

import importlib.util
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
REVIEWER = ROOT
POLICIES = sorted((REVIEWER / "policies").glob("*.md"))
DOCTRINE = sorted((REVIEWER / "doctrine").glob("*.md"))
CASES = sorted((REVIEWER / "cases").glob("*/*.md"))

POLICY_REQUIRED = (
    "policy_id",
    "subject",
    "summary",
    "model_class",
    "evidence",
    "quotable_name",
    "graded",
    "quotes_code",
)
POLICY_OPTIONAL = ("ceiling",)
MODEL_CLASSES = ("small", "medium", "large")
EVIDENCE = ("description", "scope", "commits", "patches")
GRADES = ("warn", "fail")
CASE_LINES = ("title", "expect", "grade", "why", "commit", "file")
CLAUSE = re.compile(r"\*\*([A-Z]+-\d+)\. (.+?)\.\*\*")
CASE_NAME = re.compile(r"^(clean|seeded)-(\d\d)-[a-z0-9-]+\.md$")
FILE_LINE = re.compile(r"^(\S+) \+\d+ -\d+$")
ID = re.compile(r"^[A-Z]+-\d+$")


def header_of(text: str) -> tuple[list[tuple[str, str]], str]:
    """The header's key-value lines in order, and the text after the
    three dashes."""
    header, separator, rest = text.partition("\n---\n")
    assert separator, "no --- line after the header"
    lines = []
    for line in header.split("\n"):
        if line.startswith("| ") or line == "|":
            lines.append(("|", line[2:]))
            continue
        key, colon, value = line.partition(":")
        assert colon, f"header line {line!r} is not key: value"
        lines.append((key, value.strip()))
    return lines, rest


def policy_of(path: Path) -> dict:
    lines, rest = header_of(path.read_text())
    policy: dict = {"path": path, "clauses": {}}
    for key, value in lines:
        if key == "clause":
            clause_id, _, name = value.partition(" ")
            policy["clauses"][clause_id] = name
        else:
            assert key not in policy, f"{path.name}: two {key} lines"
            policy[key] = value
    instructions, separator, notes = rest.partition("\n=== calibration\n")
    policy["instructions"] = instructions
    policy["notes"] = notes if separator else None
    return policy


def case_of(path: Path) -> dict:
    lines, rest = header_of(path.read_text())
    case: dict = {
        "path": path,
        "policy": path.parent.name,
        "lines": lines,
        "files": [],
        "body": rest,
    }
    for key, value in lines:
        if key == "file":
            case["files"].append(value)
        elif key != "|" and key != "commit":
            assert key not in case, f"{path}: two {key} lines"
            case[key] = value
    return case


def reviewer_of() -> dict:
    lines, _ = header_of((REVIEWER / "manifest.md").read_text())
    fields = dict(lines)
    return {
        "policies": [one.strip() for one in fields["policies"].split(",")],
        "checks": [one.split() for one in fields.get("checks", "").split(",") if one.strip()],
    }


def ids_in(expect: str) -> list[str]:
    return [one.strip() for one in re.split(r"[,|]", expect) if one.strip()]


DOCTRINE_TEXT = "\n\n".join(path.read_text() for path in DOCTRINE)
CLAUSES = CLAUSE.findall(DOCTRINE_TEXT)
CLAUSE_IDS = {clause_id for clause_id, _ in CLAUSES}
POLICY_BY_ID = {policy_of(path)["policy_id"]: policy_of(path) for path in POLICIES}


# The doctrine


def test_each_clause_id_is_used_once() -> None:
    seen = [clause_id for clause_id, _ in CLAUSES]
    assert len(seen) == len(set(seen)), sorted(
        one for one in seen if seen.count(one) > 1
    )


# The policies


@pytest.mark.parametrize("path", POLICIES, ids=lambda p: p.name)
def test_the_policy_header_holds_the_lines_the_server_reads(path: Path) -> None:
    policy = policy_of(path)
    keys = {key for key in policy if key not in ("path", "clauses", "instructions", "notes")}
    assert set(POLICY_REQUIRED) <= keys, f"missing {set(POLICY_REQUIRED) - keys}"
    assert keys <= set(POLICY_REQUIRED) | set(POLICY_OPTIONAL), (
        f"unknown {keys - set(POLICY_REQUIRED) - set(POLICY_OPTIONAL)}"
    )
    assert policy["model_class"] in MODEL_CLASSES
    assert policy["evidence"] in EVIDENCE
    assert policy["graded"] in ("yes", "no")
    assert policy["quotes_code"] in ("yes", "no")
    assert policy.get("ceiling", "fail") in GRADES
    assert policy["clauses"], "no clause line"


@pytest.mark.parametrize("path", POLICIES, ids=lambda p: p.name)
def test_the_policy_id_opens_its_filename(path: Path) -> None:
    policy = policy_of(path)
    assert ID.match(policy["policy_id"])
    assert path.name.startswith(policy["policy_id"] + "-")


@pytest.mark.parametrize("path", POLICIES, ids=lambda p: p.name)
def test_the_policy_cites_clauses_the_doctrine_has(path: Path) -> None:
    policy = policy_of(path)
    assert set(policy["clauses"]) <= CLAUSE_IDS, (
        set(policy["clauses"]) - CLAUSE_IDS
    )


@pytest.mark.parametrize("path", POLICIES, ids=lambda p: p.name)
def test_the_policy_has_instructions_and_calibration_notes(path: Path) -> None:
    policy = policy_of(path)
    assert policy["instructions"].strip(), "no instructions"
    assert policy["notes"] is not None, "no === calibration line"
    assert policy["notes"].strip(), "no calibration notes"


# The manifest


def test_the_reviewer_lists_each_policy_file_and_each_check() -> None:
    reviewer = reviewer_of()
    checked = {check[1] for check in reviewer["checks"]}
    assert set(reviewer["policies"]) == set(POLICY_BY_ID) | checked


def test_each_check_reports_under_a_clause_the_doctrine_has() -> None:
    for name, policy_id, clause_id in reviewer_of()["checks"]:
        assert clause_id in CLAUSE_IDS, f"{name} reports under {clause_id}"


# The cases


@pytest.mark.parametrize("path", CASES, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_the_case_is_in_a_policy_directory_and_named_for_its_kind(path: Path) -> None:
    assert path.parent.name in POLICY_BY_ID, "not a policy's directory"
    assert CASE_NAME.match(path.name), "not clean-<nn>-<name>.md or seeded-<nn>-<name>.md"


def test_case_numbers_do_not_repeat() -> None:
    repeated = []
    for directory in sorted({path.parent for path in CASES}):
        numbers = [path.name[:9] for path in directory.glob("*.md")]
        repeated += [
            f"{directory.name}/{one}" for one in set(numbers) if numbers.count(one) > 1
        ]
    assert not repeated


@pytest.mark.parametrize("path", CASES, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_the_case_header_holds_only_the_lines_a_case_may_have(path: Path) -> None:
    case = case_of(path)
    keys = [key for key, _ in case["lines"]]
    assert set(keys) <= set(CASE_LINES) | {"|"}, set(keys) - set(CASE_LINES)
    assert keys[0] == "title"
    assert "expect" in keys
    for i, key in enumerate(keys):
        if key == "|":
            assert keys[i - 1] in ("commit", "|"), "a | line must follow a commit line"
    for value in case["files"]:
        assert FILE_LINE.match(value), f"file line {value!r} is not <path> +<n> -<n>"


@pytest.mark.parametrize("path", CASES, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_the_case_says_why(path: Path) -> None:
    case = case_of(path)
    assert case.get("why"), "no why line"


@pytest.mark.parametrize("path", CASES, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_a_clean_case_expects_nothing(path: Path) -> None:
    case = case_of(path)
    if path.name.startswith("clean-"):
        assert case["expect"] == "", "a clean case expects no clause"
        assert "grade" not in case, "a clean case has no grade"


@pytest.mark.parametrize("path", CASES, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_a_seeded_case_expects_a_clause_its_policy_judges(path: Path) -> None:
    case = case_of(path)
    if path.name.startswith("seeded-"):
        expected = ids_in(case["expect"])
        assert expected, "a seeded case expects a clause"
        judged = set(POLICY_BY_ID[case["policy"]]["clauses"])
        assert set(expected) <= judged, set(expected) - judged


@pytest.mark.parametrize("path", CASES, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_a_seeded_case_of_a_graded_policy_has_a_grade(path: Path) -> None:
    case = case_of(path)
    if not path.name.startswith("seeded-"):
        return
    if POLICY_BY_ID[case["policy"]]["graded"] != "yes":
        return
    assert "grade" in case, "no grade line"
    for part in case["grade"].split(","):
        words = part.split()
        assert words[-1] in GRADES, f"grade {part.strip()!r}"
        if len(words) == 2:
            assert words[0] in ids_in(case["expect"]), f"grade names {words[0]}"
        else:
            assert len(words) == 1, f"grade {part.strip()!r}"


@pytest.mark.parametrize("path", CASES, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_each_patch_in_the_case_names_a_listed_file(path: Path) -> None:
    case = case_of(path)
    listed = {value.split(" ")[0] for value in case["files"]}
    for line in case["body"].split("\n"):
        if line.startswith("=== patch "):
            assert line[len("=== patch "):] in listed, line


# The site


def test_the_site_builds(tmp_path: Path) -> None:
    pytest.importorskip("markdown")
    spec = importlib.util.spec_from_file_location("build", ROOT / "site" / "build.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.build(ROOT, tmp_path)
    assert (tmp_path / "index.html").exists()
    assert (tmp_path / "doctrine" / "index.html").exists()
    for policy_id in POLICY_BY_ID:
        assert (tmp_path / "policies" / policy_id / "index.html").exists()
