.PHONY: skills check hooks

skills:
	python3 tools/compile.py

check:
	uv run --with pytest pytest -q

hooks:
	git config core.hooksPath .githooks
