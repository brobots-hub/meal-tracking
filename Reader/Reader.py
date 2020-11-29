import rdm6300
from Request import Request


class Reader(rdm6300.Reader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quit_loop = False

    def set_card_callback(self, callback):
        self._callback = callback

    def execute(self):
        while not self.quit_loop:
            result = self.read()
            self._callback(result)


class TestReader:
    def __init__(self, *args, **kwargs):
        pass

    def set_card_callback(self, callback):
        self._callback = callback

    def execute(self):
        self._callback('1')


if __name__ == '__main__':
    reader = Reader('/dev/serial0')
    reader.start()
