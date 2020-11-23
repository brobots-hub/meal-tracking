from os import environ

from common import load_config
from GoogleSheetsStorage import GoogleSheetsStorage
from Handlers import WriteIDs, UserChooser
from Reader import Reader, TestReader

load_config()

if environ.get('ENVIRONMENT') == 'DEVELOPMENT':
    Reader = TestReader

storage = GoogleSheetsStorage(
    environ.get('DOCUMENT_ID'),
    environ.get('SERVICE_ACCOUNT'),
    environ.get('SCOPES').split(','),
)

reader = Reader('/dev/serial0')
user_cli = UserChooser(storage)
write_id = WriteIDs(storage)

reader.set_delay(5)
reader.set_card_callback(user_cli.handle)
user_cli.set_next(write_id)

if __name__ == '__main__':
    reader.start()
