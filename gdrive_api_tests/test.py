import unittest
from handlers import api


class GDriveTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gdrive = api.GDriveAPI()

    def test1_login(self):
        self.assertTrue(self.gdrive.login_check(), "Login failed")

    def test2_upload(self):
        self.gdrive.simple_upload("/home/xantek/Code/Python/Testing_project/DataExamples/Downloader_Diablo2_plPL.exe", metadata={'name': 'Downloader_Diablo2_plPL.exe'})
        self.assertTrue(self.gdrive.find_by_id(self.gdrive.upload_id), "File not available on gDrive")

    def test3_download(self):
        self.gdrive.download(self.gdrive.upload_id, dest="test.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        pass
