from Handlers.BaseHandler import BaseHandler


class SaveData(BaseHandler):
    def __init__(self, storage):
        super().__init__()
        self._storage = storage

    def _save_data(self, data):
        self._storage.write_record(data)
        return data

    def handle(self, request):
        result = self._save_data(request)
        super().handle(result)
