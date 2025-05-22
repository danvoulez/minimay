import json
import os
from pathlib import Path
from supabase import create_client

FALLBACK_PATH = Path(os.environ.get('LOG_FALLBACK_PATH', 'logline.voulezvous.jsonl'))
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')


def load_events():
    if not FALLBACK_PATH.exists():
        return []
    with FALLBACK_PATH.open('r') as f:
        return [json.loads(line) for line in f if line.strip()]

def save_events(events):
    with FALLBACK_PATH.open('w') as f:
        for ev in events:
            f.write(json.dumps(ev) + '\n')


def main():
    if not SUPABASE_URL or not SUPABASE_KEY:
        print('Supabase not configured')
        return
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    events = load_events()
    remaining = []
    for ev in events:
        try:
            client.table('loglines').insert(ev).execute()
        except Exception:
            remaining.append(ev)
    save_events(remaining)
    print(f'Synchronized {len(events) - len(remaining)} events, remaining {len(remaining)}')


if __name__ == '__main__':
    main()
