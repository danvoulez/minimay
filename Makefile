install:
	bash install.sh

run:
	flask --app backend.app run && cd frontend && npm run build

sync:
	python backend/sync_fallback.py

test:
	python -m unittest discover tests

clean:
	rm -f logline.voulezvous.jsonl
