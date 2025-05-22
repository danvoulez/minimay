from flask import Flask, request, jsonify
from supabase import create_client, Client
import json
import os
from pathlib import Path

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
