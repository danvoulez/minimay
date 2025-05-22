try:
    from flask import Flask, request, jsonify, Response
except ModuleNotFoundError:  # minimal fallback to run tests without flask
    import json as _json

    class Request:
        def __init__(self):
            self._json = None
            self._data = b""

        def get_json(self):
            return self._json

        @property
        def data(self):
            return self._data

    request = Request()

    class Response:
        def __init__(self, data=None, status=200):
            self.data = (
                data.encode() if isinstance(data, str) else (data or b"")
            )
            self.status_code = status

    def jsonify(obj):
        return Response(_json.dumps(obj), 200)

    class Flask:
        def __init__(self, name):
            self.routes = {}

        def route(self, path, methods=None):
            if methods is None:
                methods = ["GET"]

            def decorator(fn):
                for m in methods:
                    self.routes[(path, m)] = fn
                return fn

            return decorator

        def test_client(self):
            app = self

            class Client:
                def post(self, path, json=None, data=None):
                    request._json = json
                    request._data = (data.encode() if isinstance(data, str) else data) or b""
                    func = app.routes.get((path, "POST"))
                    if not func:
                        return Response(status=404)
                    result = func()
                    if isinstance(result, Response):
                        return result
                    if isinstance(result, tuple):
                        body, status = result
                        if isinstance(body, Response):
                            body.status_code = status
                            return body
                        return Response(_json.dumps(body), status)
                    return Response(_json.dumps(result), 200)

            return Client()

from typing import Optional

try:
    from supabase import create_client, Client
except ModuleNotFoundError:  # allow running without supabase package
    create_client = None
    Client = None
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    def load_dotenv(*args, **kwargs):
        return None
import json
import os
from pathlib import Path

from .llm_service import parse_text_to_logline

load_dotenv()
app = Flask(__name__)

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
FALLBACK_PATH = Path(os.environ.get('LOG_FALLBACK_PATH', 'logline.voulezvous.jsonl'))

supabase = None
if SUPABASE_URL and SUPABASE_KEY and create_client:
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
