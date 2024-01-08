import os
import unittest
import shutil

from able import DeleterString


class TestDeleterString(unittest.TestCase):

    def setUp(self):
        #print('A')
        self.folder = '{}/Development/Temp/deleter_string'.format(os.environ['HOME'])
        self.folder_filename = '{}/deleter.txt'.format(self.folder)
        self.contents = 'A=a\nB=b'
        os.makedirs(self.folder, exist_ok=True)
        with open(self.folder_filename, 'w') as f:
            f.write(self.contents)

    def tearDown(self):
        fileExists = os.path.isfile(self.folder_filename)
        if fileExists:
            shutil.rmtree(self.folder)

    def test_init(self):
        actual = DeleterString(self.folder_filename)
        # print('actual', actual.replace('\n',''))
        assert (actual == self.contents)
        assert (not os.path.isfile(self.folder_filename))

if __name__ == '__main__':
    unittest.main()