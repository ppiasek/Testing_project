import unittest
from handlers import api
from pathlib import Path

UPLOAD_DATA_PATH = '../data_examples/Downloader_Diablo2_plPL.exe'
UPLOAD_METADATA = {'name': 'Downloader_Diablo2_plPL.exe'}
DOWNLOAD_NAME = UPLOAD_METADATA['name']


class GDriveTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gdrive = api.GDriveAPI()

    def test1_login(self):
        self.assertTrue(self.gdrive.login_check(), "Login failed")

    def test2_upload(self):
        self.gdrive.simple_upload(Path(UPLOAD_DATA_PATH), metadata=UPLOAD_METADATA)
        self.assertTrue(self.gdrive.find_by_id(self.gdrive.upload_id), "File not available on gDrive")

    def test3_download(self):
        self.gdrive.download(self.gdrive.upload_id, dest=DOWNLOAD_NAME)

    @classmethod
    def tearDownClass(cls) -> None:
        pass
