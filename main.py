from Authenticator import Authenticator
from common import load_config
from GoogleSheetsStorage import GoogleSheetsStorage
from Reader import Reader

load_config()

storage = GoogleSheetsStorage()
