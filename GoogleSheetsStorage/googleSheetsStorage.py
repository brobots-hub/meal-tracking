from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleSheetsStorage:
    def __init__(self, service_account_file, scopes):
        creds = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=scopes)

        service = build('sheets', 'v4', credentials=creds)
        self._sheet = service.spreadsheets()

    def get_students(self):
        pass

    def get_student_by_id(self, student_id):
        pass


if __name__ == '__main__':
    storage = GoogleSheetsStorage()
