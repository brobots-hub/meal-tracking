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

    def write_record(self, data: Request):
        user_row = self._find_user_row(data.id)
        if not user_row:
            return False

        records_col = environ.get('RECORDS_COL')
        empty_col = self._get_first_empty_col(records_col, user_row)

        body = {
            'values': [
                [str(data.date)]
            ]
        }

        result = self._sheet.values().update(
            spreadsheetId=self._document_id,
            range='{0}{1}'.format(empty_col, user_row),
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()

        return True if result.get('updatedRange', False) else False

    def _find_user_row(self, user_id):
        users = self.get_users()
        first_row = int(environ.get('FIRST_ROW'))
        user_row = None

        i = 0
        for user in users:
            if user == user_id:
                user_row = i + first_row
                break
            i += 1

        if user_row == None:
            return False

        return user_row

    def _get_first_empty_col(self, start_col, row):
        result = self._sheet.values()\
            .get(spreadsheetId=self._document_id, range=self._get_records_range(row))\
            .execute()\
            .get('values', [[]])[0]

        return chr(ord(start_col) + len(result))

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

    def _get_records_range(self, user_row):
        return '{0}{1}:{2}'.format(
            environ.get('RECORDS_COL'),
            user_row,
            5000
        )


if __name__ == '__main__':
    storage = GoogleSheetsStorage()
