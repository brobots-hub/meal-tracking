from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleSheetsStorage:
    def __init__(self, document_id, service_account, scopes):
        creds = service_account.Credentials.from_service_account_file(
            service_account, scopes=scopes)

        service = build('sheets', 'v4', credentials=creds)
        self._sheet = service.spreadsheets()
        self._document_id = document_id

    def get_students(self):
        pass

    def get_student_by_id(self, user_id):
        pass


if __name__ == '__main__':
    storage = GoogleSheetsStorage()
