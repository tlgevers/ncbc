from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class MusicHandler():
    def _get_drive_service(self):
        from apiclient import discovery
        from oauth2client.service_account import ServiceAccountCredentials
        from httplib2 import Http
        scopes = ['https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CONFIG_CALENDAR, scopes)
        http_auth = credentials.authorize(Http(timeout=60))
        service = discovery.build('drive', 'v3', http=http_auth)
        return service
