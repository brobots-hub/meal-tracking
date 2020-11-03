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
        users = self.get_users()
        meals_col = environ.get('MEALS_COL')
        first_row = int(environ.get('FIRST_ROW'))
        user_row = None

        i = 0
        for user in users:
            if user == data.id:
                user_row = i + first_row
                break
            i += 1

        if user_row == None:
            return False

        result = self._sheet.values()\
            .get(spreadsheetId=self._document_id, range=self._get_meals_range(user_row))\
            .execute()\
            .get('values', [[]])[0]

        write_col = chr(ord(meals_col) + len(result))

        body = {
            'values': [
                [str(data.date)]
            ]
        }

        result = self._sheet.values().update(
            spreadsheetId=self._document_id,
            range='{0}{1}'.format(write_col, user_row),
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()

    def get_user_by_id(self, user_id):
        users = self.get_users()

        if users:
            return users.get(str(user_id), False)

        return users

    def get_users(self):
        users = self._sheet.values()\
            .get(spreadsheetId=self._document_id, range=self._get_users_range())\
            .execute()\
            .get('values', False)

        result = {user[0]: user[1] for user in users}
        return result

    def _get_users_range(self):
        return '{0}{1}:{2}'.format(
            environ.get('USER_ID_COL'),
            environ.get('FIRST_ROW'),
            environ.get('USER_NAME_COL'),
        )

    def _get_meals_range(self, user_row):
        return '{0}{1}:{2}'.format(
            environ.get('MEALS_COL'),
            user_row,
            5000
        )


if __name__ == '__main__':
    storage = GoogleSheetsStorage()
