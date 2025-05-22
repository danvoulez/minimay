import unittest
import os
import json
from pathlib import Path



class AppTest(unittest.TestCase):
    def test_register_fallback(self):
        path = Path('test_fallback.jsonl')
        os.environ['LOG_FALLBACK_PATH'] = str(path)
        import importlib
        import backend.app as app
        importlib.reload(app)
        client = app.app.test_client()
        resp = client.post(
            '/register',
            json={'who': 'a', 'did': 'b', 'this': 'c', 'when': 'now', 'confirmed_by': '', 'if_ok': '', 'if_doubt': '', 'if_not': '', 'status': 'pending'}
        )
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data.decode())
        self.assertEqual(data['status'], 'fallback')
        self.assertTrue(path.exists())
        path.unlink()


if __name__ == '__main__':
    unittest.main()
