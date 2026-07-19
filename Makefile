.PHONY: help install sync lock test test-live clean build publish

help:
	@echo "Available targets:"
	@echo "  install    Install package with dev dependencies"
	@echo "  sync       Sync environment with lockfile"
	@echo "  lock       Update the lockfile"
	@echo "  test       Run tests (excludes live tests)"
	@echo "  test-live  Run all tests including live"
	@echo "  clean      Remove build artifacts and caches"
	@echo "  build      Build sdist and wheel"
	@echo "  publish    Publish to PyPI"

install:
	uv sync --all-extras --dev

sync:
	uv sync

lock:
	uv lock

test:
	uv run pytest

test-live:
	uv run pytest -m ""

clean:
	rm -rf dist build *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

build: clean
	uv build

publish: build
	uv publish
