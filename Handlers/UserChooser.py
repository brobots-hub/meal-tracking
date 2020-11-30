import enquiries

from Handlers.BaseHandler import BaseHandler


class UserChooser(BaseHandler):
    def __init__(self, storage):
        super().__init__()
        self._storage = storage

    def _get_user_name(self):
        users = self._storage.get_users()
        options = []

        for user in users:
            options.append(
                ' '.join((user[0].ljust(8),
                          user[1])
                         )
            )

        choice = enquiries.choose('Choose a user: ', options)
        return choice[9:]

    def handle(self, request):
        user_name = self._get_user_name()
        request.name = user_name
        super().handle(request)
