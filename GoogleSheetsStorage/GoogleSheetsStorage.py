import logging
from os import environ

from google.oauth2 import service_account
from googleapiclient.discovery import build
from Request import Request


class GoogleSheetsStorage:
    def __init__(self, document_id, account_key, scopes):
        creds = service_account.Credentials.from_service_account_file(
            account_key, scopes=scopes)

        service = build('sheets', 'v4', credentials=creds,
                        cache_discovery=False)
        self._sheet = service.spreadsheets()
        self._document_id = document_id

    def write_user_id(self, user_id, user_name):
        try:
            return self._write_user_id(user_id, user_name)
        except:
            logging.critical('google sheets request error')

    def _write_user_id(self, user_id, user_name):
        user_row = self._find_user_row_by_name(user_name)
        ids_col = environ.get('USER_ID_COL')

        body = {
            'values': [
                [str(user_id)]
            ]
        }

        result = self._sheet.values().update(
            spreadsheetId=self._document_id,
            range='{0}{1}'.format(ids_col, user_row),
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()

        logging.debug(f'user id updated - {user_id}')
        return True if result.get('updatedRange', False) else False

    def _find_user_row_by_name(self, user_name):
        users = self.get_users()
        first_row = int(environ.get('FIRST_ROW'))
        user_row = False

        if not users:
            return user_row

        i = 0
        for user in users:
            if user[1] == user_name:
                user_row = i + first_row
                break
            i += 1

        return user_row

    def write_record(self, data: Request):
        try:
            return self._write_record(data)
        except:
            logging.critical(
                'google sheets request error - probably row overflow')

    def _write_record(self, data: Request):
        user_row = self._find_user_row_by_id(data.id)

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

        logging.debug(f'user record saved - {data}')
        return True if result.get('updatedRange', False) else False

    def _find_user_row_by_id(self, user_id):
        users = self.get_users()
        first_row = int(environ.get('FIRST_ROW'))
        user_row = False

        if not users:
            return user_row

        i = 0
        for user in users:
            if user[0] == user_id:
                user_row = i + first_row
                break
            i += 1

        return user_row

    def _get_first_empty_col(self, start_col, row):
        result = self._sheet.values()\
            .get(spreadsheetId=self._document_id, range=self._get_records_range(row))\
            .execute()\
            .get('values', [[]])[0]

        return chr(ord(start_col) + len(result))

    def get_user_by_id(self, user_id):
        users = self.get_users()

        if not users:
            return False

        for user in users:
            if user[0] == user_id:
                return user

    def get_users(self):
        users = self._sheet.values()\
            .get(spreadsheetId=self._document_id, range=self._get_users_range())\
            .execute()\
            .get('values', False)

        return users

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
