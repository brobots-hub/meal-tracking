from Handlers.BaseHandler import BaseHandler


class WriteIDs(BaseHandler):
    def __init__(self, storage):
        super().__init__()
        self._storage = storage

    def _update_data(self, data):
        self._storage.write_user_id(data.id, data.name)
        return data

    def handle(self, request):
        result = self._update_data(request)
        super().handle(result)
