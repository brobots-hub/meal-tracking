class Request:
    def __init__(self, user_id='', user_name='', user_row='', meal_type=''):
        self.id = user_id
        self.name = user_name
        self.row = user_row
        self.meal_type = meal_type

    def __repr__(self):
        return f'<Request from user "{self.name}">'
