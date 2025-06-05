import json as json_mod

class _Request:
    def __init__(self):
        self._json = None
        self.data = b''

    def get_json(self):
        return self._json

request = _Request()

class Response:
    def __init__(self, data, status=200):
        self.data = data.encode() if isinstance(data, str) else data
        self.status_code = status


def jsonify(obj):
    return Response(json_mod.dumps(obj), 200)

class Flask:
    def __init__(self, name):
        self.name = name
        self._routes = {}

    def route(self, path, methods=None):
        methods = tuple((methods or ['GET']))
        def decorator(func):
            self._routes[(path, methods)] = func
            return func
        return decorator

    def test_client(self):
        app = self

        class Client:
            def post(self, path, json=None, data=None):
                request._json = json
                request.data = data.encode() if isinstance(data, str) else (data or b'')
                func = app._routes.get((path, ('POST',)))
                rv = func()
                if isinstance(rv, Response):
                    return rv
                if isinstance(rv, tuple):
                    body, status = rv
                    if isinstance(body, Response):
                        body.status_code = status
                        return body
                    return Response(json_mod.dumps(body), status)
                return Response(str(rv))
        return Client()
