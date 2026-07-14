release:
	cargo build --release

setup_test: release
	python -m venv .venv
	source .venv/bin/activate
	pip install -r tests/requirements.txt
	deactivate

test: setup_test
	.venv/bin/pytest

setup_test_win: release
	python -m venv .venv
	source .venv/Scripts/activate
	pip install -r tests/requirements.txt
	deactivate

test_win: setup_test
	.venv/Scripts\pytest