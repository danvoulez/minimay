import json

class Request:
    def __init__(self, json_data=None, data=b''):
        self._json = json_data
        self.data = data
    def get_json(self):
        return self._json

request = Request()

class Response:
    def __init__(self, data, status=200):
        self.data = data if isinstance(data, bytes) else json.dumps(data).encode()
        self.status_code = status

class Flask:
    def __init__(self, name):
        self.routes = {}
    def route(self, path, methods=['GET']):
        def decorator(f):
            for m in methods:
                self.routes[(path, m.upper())] = f
            return f
        return decorator
    def test_client(self):
        app = self
        class Client:
            def post(self, path, json=None, data=None):
                handler = app.routes.get((path, 'POST'))
                if not handler:
                    return Response({'error':'not found'}, 404)
                global request
                request = Request(json, data.encode() if isinstance(data,str) else data or b'')
                result = handler()
                if isinstance(result, tuple):
                    body, status = result
                else:
                    body, status = result, 200
                return Response(body, status)
            def get(self, path):
                handler = app.routes.get((path, 'GET'))
                if not handler:
                    return Response({'error':'not found'}, 404)
                result = handler()
                if isinstance(result, tuple):
                    body, status = result
                else:
                    body, status = result, 200
                return Response(body, status)
        return Client()

def jsonify(obj):
    return obj
