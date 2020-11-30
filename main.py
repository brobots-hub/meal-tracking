import logging
from os import environ

from common import load_config
from GoogleSheetsStorage import GoogleSheetsStorage
from Handlers import Authenticator, SaveData
from Reader import Reader, TestReader

load_config()
logging.basicConfig(filename=environ.get('LOGFILE', 'app.log'),
                    level=environ.get('LOGLEVEL', 'INFO'))

if environ.get('ENVIRONMENT') == 'DEVELOPMENT':
    Reader = TestReader

storage = GoogleSheetsStorage(
    environ.get('DOCUMENT_ID'),
    environ.get('SERVICE_ACCOUNT'),
    environ.get('SCOPES').split(','),
)

reader = Reader('/dev/serial0')
auth = Authenticator(storage)
save_data = SaveData(storage)

reader.set_card_callback(auth.handle)
auth.set_next(save_data)

if __name__ == '__main__':
    reader.start()
