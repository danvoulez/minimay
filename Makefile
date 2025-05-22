install:
	bash install.sh

test:
	python -m pytest -q

sync:
	python backend/sync_fallback.py
