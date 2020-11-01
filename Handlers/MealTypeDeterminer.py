from Handlers.BaseHandler import BaseHandler


class MealTypeDeterminer(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self, request):
        request.meal_type = 'lunch'
        result = request

        super().handle(result)
