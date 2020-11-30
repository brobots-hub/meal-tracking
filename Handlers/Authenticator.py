import logging

from Handlers.BaseHandler import BaseHandler


class Authenticator(BaseHandler):
    def __init__(self, storage):
        super().__init__()
        self._storage = storage

    def _authenticate(self, data):
        user = self._storage.get_user_by_id(data.id)

        if not user:
            logging.warning(f'user with such credentials not found - {data}')

        return user if user else False

    def handle(self, request):
        result = self._authenticate(request)
        request.name = result

        if result:
            logging.debug(f'successfully authenticated user - {request}')
            super().handle(request)


if __name__ == '__main__':
    auth = Authenticator()
