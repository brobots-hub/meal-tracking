from Handlers.BaseHandler import BaseHandler


class Authenticator(BaseHandler):
    def __init__(self, storage):
        super().__init__()
        self._storage = storage

    def _authenticate(self, data):
        user = self._storage.get_user_by_id(data.id)
        return user if user else False

    def handle(self, request):
        result = self._authenticate(request)

        super().handle(result)


if __name__ == '__main__':
    auth = Authenticator()
