from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake!'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_without_params()
        )
        return json.dumps(body)

    def get_headers(self, environ=None):
        return [('content-Type', 'application/json')]

    @staticmethod
    def get_url_without_params():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]
