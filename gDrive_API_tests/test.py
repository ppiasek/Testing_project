from Handlers import API
import unittest


class gDrive_tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gDrive = API.GDriveAPI()

    def test1Login(self):
        self.assertTrue(self.gDrive.login_check() == True, "Login failed")

    def test2Upload(self):
        self.gDrive.simple_upload("/home/xantek/Code/Python/Testing_project/DataExamples/Downloader_Diablo2_plPL.exe", metadata={'name' : 'Downloader_Diablo2_plPL.exe'})
        self.assertTrue(self.gDrive.find_by_id(self.gDrive.upload_id) == True, "File not available on gDrive")

    def test3Download(self):
        self.gDrive.download(self.gDrive.upload_id, dest="test.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.gDrive