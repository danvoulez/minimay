try:
    from flask import Flask, request, jsonify
except ModuleNotFoundError:  # pragma: no cover - testing without Flask
    from .flask_stub import Flask, request, jsonify

try:
    from supabase import create_client, Client
except ModuleNotFoundError:  # pragma: no cover - testing without supabase
    class _DummyTable:
        def insert(self, _):
            return self

        def execute(self):
            return None

    class _DummyClient:
        def table(self, _):
            return _DummyTable()

    def create_client(url, key):  # noqa: D401
        """Return a dummy supabase client when package is missing."""
        return _DummyClient()

    Client = _DummyClient

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:  # pragma: no cover - testing without dotenv
    def load_dotenv():
        return None
import json
import os
from pathlib import Path

from .llm_service import parse_text_to_logline, interpretar_frase

load_dotenv()
app = Flask(__name__)

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
FALLBACK_PATH = Path(os.environ.get('LOG_FALLBACK_PATH', 'logline.voulezvous.jsonl'))

supabase: Client | None = None
if SUPABASE_URL and SUPABASE_KEY:
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception:
        supabase = None


def save_fallback(logline: dict) -> None:
    logline['origem'] = 'fallback'
    with FALLBACK_PATH.open('a') as f:
        f.write(json.dumps(logline) + '\n')


def load_events():
    if not FALLBACK_PATH.exists():
        return []
    with FALLBACK_PATH.open('r') as f:
        return [json.loads(line) for line in f if line.strip()]

def save_events(events):
    with FALLBACK_PATH.open('w') as f:
        for ev in events:
            f.write(json.dumps(ev) + '\n')


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        text = request.data.decode('utf-8')
        if not text:
            return jsonify({'error': 'No data provided'}), 400
        logline = interpretar_frase(text)
    else:
        if isinstance(data, str):
            logline = interpretar_frase(data)
        else:
            logline = data

    if supabase:
        try:
            supabase.table('loglines').insert(logline).execute()
            return jsonify({'status': 'ok'})
        except Exception as e:
            save_fallback(logline)
            return jsonify({'status': 'fallback', 'error': str(e)}), 500
    else:
        save_fallback(logline)
        return jsonify({'status': 'fallback'}), 200


@app.route('/prompts', methods=['GET'])
def get_prompts():
    path = Path('prompts.extended 2.json')
    try:
        with path.open() as f:
            data = json.load(f)
    except Exception:
        data = []
    return jsonify(data)


@app.route('/timeline', methods=['GET'])
def timeline():
    if supabase:
        try:
            data = supabase.table('loglines').select('*').execute().data
            return jsonify(data)
        except Exception:
            pass
    if FALLBACK_PATH.exists():
        with FALLBACK_PATH.open() as f:
            entries = [json.loads(line) for line in f if line.strip()]
        return jsonify(entries)
    return jsonify([])


@app.route('/sync', methods=['POST'])
def sync():
    if not SUPABASE_URL or not SUPABASE_KEY:
        return jsonify({'error': 'Supabase not configured'}), 500
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    events = load_events()
    remaining = []
    for ev in events:
        try:
            client.table('loglines').insert(ev).execute()
        except Exception:
            remaining.append(ev)
    save_events(remaining)
    return jsonify({'synchronized': len(events) - len(remaining), 'remaining': len(remaining)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
