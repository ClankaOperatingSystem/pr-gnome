.PHONY: skills check

skills:
	python3 tools/compile.py

check:
	uv run --with pytest pytest -q
