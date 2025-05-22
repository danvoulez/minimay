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

def test_register_supabase(monkeypatch):
    monkeypatch.setenv('SUPABASE_URL', 'http://localhost')
    monkeypatch.setenv('SUPABASE_KEY', 'test_key')
    client = app.test_client()
    resp = client.post('/register', json={'who':'a','did':'b','this':'c','when':'now','confirmed_by':'','if_ok':'','if_doubt':'','if_not':'','status':'pending'})
    assert resp.status_code == 200
    data = json.loads(resp.data.decode())
    assert data['status'] == 'ok'

def test_get_prompts():
    client = app.test_client()
    resp = client.get('/prompts')
    assert resp.status_code == 200
    data = json.loads(resp.data.decode())
    assert isinstance(data, list)

def test_timeline_fallback(tmp_path, monkeypatch):
    path = tmp_path / 'fallback.jsonl'
    monkeypatch.setenv('LOG_FALLBACK_PATH', str(path))
    save_fallback({'who':'a','did':'b','this':'c','when':'now','confirmed_by':'','if_ok':'','if_doubt':'','if_not':'','status':'pending'})
    client = app.test_client()
    resp = client.get('/timeline')
    assert resp.status_code == 200
    data = json.loads(resp.data.decode())
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['who'] == 'a'
