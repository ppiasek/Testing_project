from __future__ import print_function
import io
import os.path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import *

SCOPES = ['https://www.googleapis.com/auth/drive']
TOKEN = '../credentials/token.pickle'
JSON_CREDENTIALS = '../credentials/credentials.json'


class GDriveAPI(object):

    def __init__(self):
        self._credentials = None
        self.list_files = None
        self.upload_id = None
        self.download_data = None

        if os.path.exists(TOKEN):
            with open(TOKEN, 'rb') as token:
                self._credentials = pickle.load(token)
        if not self._credentials or not self._credentials.valid:
            if self._credentials and self._credentials.expired and self._credentials.refreshTOKEN:
                self._credentials.refresh(Request())
            else:
                self._flow = InstalledAppFlow.from_client_secrets_file(
                    JSON_CREDENTIALS, SCOPES)
                self._credentials = self._flow.run_local_server(port=0)
            with open(TOKEN, 'wb') as token:
                pickle.dump(self._credentials, token)

        self.service = build('drive', 'v3', credentials=self._credentials)
        self.show_files(pagesize=1000)

    def login_check(self):
        return self.service._http.credentials.valid  # Returns certificate validity

    def show_files(self, pagesize=100):

        self.list_files = self.service.files().list(
            pageSize=pagesize, fields="files(name, size, modifiedTime, mimeType, id)").execute().get('files', [])

    def print_list_files(self):

        for items in self.list_files:
            print(items)

    def list_files_length(self):
        return len(self.list_files)

    def simple_upload(self, path, metadata=None):
        upload = MediaFileUpload(path)
        if metadata:
            upload = self.service.files().create(body=metadata, media_body=upload, fields='id').execute()
        else:
            upload = self.service.files().create(media_body=upload, fields='id').execute()
        self.upload_id = upload.get('id')

    def multipart_upload(self):
        pass

    def resumable_upload(self):
        pass

    def find_by_id(self, file_id):
        self.show_files(pagesize=1000)
        if True in map(lambda val: val['id'] == file_id, self.list_files):
            return True
        else:
            return False

    def download(self, file_id, dest="Blank.txt"):
        download_data = self.service.files().get_media(fileId=file_id)
        fh = io.FileIO(dest, 'wb')
        downloader = MediaIoBaseDownload(fh, download_data)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
        fh.close()
