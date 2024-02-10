import os
import unittest
import shutil

from able import EnvString, StringReader

class TestEnvString(unittest.TestCase):

    def setUp(self):
        self.folder = '{}/Development/Temp/env_string'.format(os.environ['HOME'])
        self.folder_filename = '{}/env_string.env'.format(self.folder)
        self.contents = 'AAAAA=a\nBBBBB=b'
        os.makedirs(self.folder, exist_ok=True)
        with open(self.folder_filename, 'w') as f:
            f.write(self.contents)

    def tearDown(self):
        fileExists = os.path.isfile(self.folder_filename)
        if fileExists:
            shutil.rmtree(self.folder)

    def test_init(self):
        assert (EnvString(StringReader(self.folder_filename)) == self.contents)
        assert (os.environ['AAAAA'] == 'a')
        assert (os.environ['BBBBB'] == 'b')

if __name__ == '__main__':
    unittest.main()