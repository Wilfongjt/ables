import os
import unittest
import shutil

from able import CreatorString
from able import ReaderString

class TestReaderString(unittest.TestCase):

    def setUp(self):
        self.folder = '{}/Development/Temp/reader_string'.format(os.environ['HOME'])
        self.folder_filename = '{}/reader.txt'.format(self.folder)
        self.contents = 'A=a\nB=b'
        os.makedirs(self.folder, exist_ok=True)
        with open(self.folder_filename, 'w') as f:
            f.write(self.contents)

    def tearDown(self):
        fileExists = os.path.isfile(self.folder_filename)
        if fileExists:
            shutil.rmtree(self.folder)

    def test_init(self):
        self.assertTrue(ReaderString(self.folder_filename)==self.contents)


if __name__ == '__main__':
    unittest.main()