import json
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    def load_dotenv():
        pass

try:
    from flask import Flask, request, jsonify
except ModuleNotFoundError:  # lightweight fallback
    class _FakeReq:
        json = None
        data = b''
    request = _FakeReq()
    def jsonify(obj):
        return obj
    class _FakeClient:
        def __init__(self, app):
            self.app = app
        def post(self, path, json=None):
            request.json = json
            resp = self.app.routes[path]()
            return type('Resp', (), {'status_code': 200, 'data': json.dumps(resp).encode()})
    class Flask:
        def __init__(self, name):
            self.routes = {}
        def route(self, path, methods=None):
            def wrapper(f):
                self.routes[path] = f
                return f
            return wrapper
        def test_client(self):
            return _FakeClient(self)
        def run(self, *a, **k):
            pass
    from types import SimpleNamespace
    create_client = lambda url, key: SimpleNamespace(table=lambda name: SimpleNamespace(insert=lambda x: None, select=lambda *a, **k: SimpleNamespace(execute=lambda: SimpleNamespace(data=[]))))
    Client = object
else:
    from supabase import create_client, Client

load_dotenv()

from .llm_service import parse_text_to_logline
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


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        text = request.data.decode('utf-8')
        if not text:
            return jsonify({'error': 'No data provided'}), 400
        logline = parse_text_to_logline(text)
    else:
        if isinstance(data, str):
            logline = parse_text_to_logline(data)
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
