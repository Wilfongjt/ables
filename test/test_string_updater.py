import os
import unittest
import shutil

from able import UpdaterString, ReaderString

class TestUpdaterString(unittest.TestCase):

    def setUp(self):
        #print('A')
        self.folder = '{}/Development/Temp/updater_string'.format(os.environ['HOME'])
        self.folder_filename = '{}/updater.txt'.format(self.folder)
        self.contents = 'A=a\nB=b'
        os.makedirs(self.folder, exist_ok=True)
        with open(self.folder_filename, 'w') as f:
            f.write(self.contents)

    def tearDown(self):
        fileExists = os.path.isfile(self.folder_filename)
        if fileExists:
            shutil.rmtree(self.folder)

    def test_init(self):
        assert (UpdaterString(self.folder_filename, 'A=', 'A=A') == 'A=A\nB=b')
        assert (ReaderString(self.folder_filename) == 'A=A\nB=b')
        assert (UpdaterString(self.folder_filename, 'B=', 'B=B') == 'A=A\nB=B')
        assert (ReaderString(self.folder_filename) == 'A=A\nB=B')
        assert (UpdaterString(self.folder_filename, 'C=', 'C=C') == 'A=A\nB=B\nC=C')
        assert (ReaderString(self.folder_filename) == 'A=A\nB=B\nC=C')

if __name__ == '__main__':
    unittest.main()