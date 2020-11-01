from Request import Request


class Reader():
    def __init__(self):
        pass

    def start(self):
        self._on_card_near('3')

    def set_card_callback(self, callback):
        self._callback = callback

    def _on_card_near(self, card_id):
        r = Request(user_id=card_id)
        self._callback(r)


if __name__ == '__main__':
    reader = Reader()
    reader.start()
