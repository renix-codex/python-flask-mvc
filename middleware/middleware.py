from flask import request, abort

class AuthorizationMiddleware:
    def __init__(self, app, authorized_tokens):
        self.app = app
        self.authorized_tokens = authorized_tokens

    def __call__(self, environ, start_response):
        authorization_header = environ.get('HTTP_AUTHORIZATION', '')
        token = authorization_header.replace('Bearer ', '')

        if token not in self.authorized_tokens:
            abort(401, "Unauthorized")

        return self.app(environ, start_response)