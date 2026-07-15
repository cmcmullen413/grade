release:
	cargo build --release

setup_test: release
	python -m venv .venv
	.venv/bin/pip install -r tests/requirements.txt

test: setup_test
	.venv/bin/pytest

setup_test_win: release
	python -m venv .venv
	.venv\Scripts\pip install -r tests\requirements.txt

test_win: setup_test
	.venv/Scripts\pytest