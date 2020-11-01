from os import environ

from common import load_config
from GoogleSheetsStorage import GoogleSheetsStorage
from Handlers import Authenticator, MealTypeDeterminer, SaveData
from Reader import Reader

load_config()

storage = GoogleSheetsStorage(
    environ.get('DOCUMENT_ID'),
    environ.get('SERVICE_ACCOUNT'),
    environ.get('SCOPES').split(','),
)

reader = Reader()
auth = Authenticator(storage)
meal_typer = MealTypeDeterminer()
save_data = SaveData(storage)

reader.set_card_callback(auth.handle)
auth.set_next(meal_typer)
meal_typer.set_next(save_data)

if __name__ == '__main__':
    reader.start()
