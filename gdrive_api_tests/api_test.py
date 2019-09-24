import unittest
from handlers import api
from pathlib import Path

upload_data_path = '../data_examples/Downloader_Diablo2_plPL.exe'
upload_metadata = {'name': 'Downloader_Diablo2_plPL.exe'}
download_name = upload_metadata['name']


class GDriveTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gdrive = api.GDriveAPI()

    def test1_login(self):
        self.assertTrue(self.gdrive.login_check(), "Login failed")

    def test2_upload(self):
        self.gdrive.simple_upload(Path(upload_data_path), metadata=upload_metadata)
        self.assertTrue(self.gdrive.find_by_id(self.gdrive.upload_id), "File not available on gDrive")

    def test3_download(self):
        self.gdrive.download(self.gdrive.upload_id, dest=download_name)

    @classmethod
    def tearDownClass(cls) -> None:
        pass
