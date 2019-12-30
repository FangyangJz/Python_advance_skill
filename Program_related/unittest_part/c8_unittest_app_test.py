import unittest
from c8_unittest_app import CountFiles

from unittest import mock

testdir = r'E:\Python_project_in_E\Python_Code_Skills\Python_advance_skill\unittest_part\testdir'

class TestApp(unittest.TestCase):

    def setUp(self):
        self.obj = CountFiles(path=testdir)

    def test_cjpeg(self):
        self.assertEqual(self.obj.cjpeg(), 1)

    def test_cpng(self):
        self.assertEqual(self.obj.cpng(), 4)

    def test_cfile(self):
        self.assertEqual(self.obj.cfile(), 2)

    def test_cdir(self):
        self.assertEqual(self.obj.cdir(), 0)

    def tearDown(self):
        self.obj = None


if __name__ == '__main__':
    unittest.main()
