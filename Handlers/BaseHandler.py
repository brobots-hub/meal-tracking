from abc import ABC, abstractmethod


class BaseHandler(ABC):
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next = next
        return next

    @abstractmethod
    def handle(self, data):
        if not self.next or not data:
            return data

        self.next.handle(data)
