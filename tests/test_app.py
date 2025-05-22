from backend.app import app, save_fallback
import json
from pathlib import Path

def test_register_fallback(tmp_path, monkeypatch):
    path = tmp_path / 'fallback.jsonl'
    monkeypatch.setenv('LOG_FALLBACK_PATH', str(path))
    client = app.test_client()
    resp = client.post('/register', json={'who':'a','did':'b','this':'c','when':'now','confirmed_by':'','if_ok':'','if_doubt':'','if_not':'','status':'pending'})
    assert resp.status_code == 200
    data = json.loads(resp.data.decode())
    assert data['status'] == 'fallback'
    assert path.exists()
