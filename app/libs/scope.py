class Scope:
    allow_api = []
    allow_module = []

    def __add___(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))
        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))
        return self


class AdminScope(Scope):
    allow_module = ['v1.user']

    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_api = ['v1.user+get_user', 'v1.user+delete_user']


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.splits('+')
    red_name = splits[0]
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
