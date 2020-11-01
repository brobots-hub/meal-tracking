from os import environ

from google.oauth2 import service_account
from googleapiclient.discovery import build
from Request import Request


class GoogleSheetsStorage:
    def __init__(self, document_id, account_key, scopes):
        creds = service_account.Credentials.from_service_account_file(
            account_key, scopes=scopes)

        service = build('sheets', 'v4', credentials=creds)
        self._sheet = service.spreadsheets()
        self._document_id = document_id

    def write_meal(self, data: Request):
        pass

    def get_user_by_id(self, user_id):
        users = self.get_users()

        if users:
            return users.get(user_id, False)

        return users

    def get_users(self):
        first_row = 2  # TODO: move spreadsheets ranges to .env file

        users = self._sheet.values()\
            .get(spreadsheetId=self._document_id, range=self._get_users_range())\
            .execute()\
            .get('values', False)

        result = {}
        for i in range(len(users)):
            u_id = str(users[i][0])
            result[u_id] = Request(
                user_id=u_id,
                user_name=users[i][1],
                user_row=i + first_row
            )

        return result if result else False

    def _get_users_range(self):
        return '{0}{1}:{2}'.format(
            environ.get('FIRST_COL'),
            environ.get('USER_ID_ROW'),
            environ.get('USER_NAME_ROW'),
        )


if __name__ == '__main__':
    storage = GoogleSheetsStorage()
