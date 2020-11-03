from datetime import datetime


class Request:
    def __init__(self, user_id='', user_name='', request_date=datetime.now()):
        self.id = user_id
        self.name = user_name
        self.date = request_date

    def __repr__(self):
        return f'<Request from "{self.id}">'
