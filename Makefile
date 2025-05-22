install:
	bash install.sh

run:
	flask --app backend.app run

sync:
	python backend/sync_fallback.py

test:
	python -m unittest discover tests

clean:
	rm -f logline.voulezvous.jsonl
