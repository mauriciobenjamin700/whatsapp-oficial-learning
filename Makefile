lint-fix:
	uv run black src tests --line-length 80
	uv run isort src tests
	uv run ruff check src tests --fix