import os
import unittest
import shutil

from able import CreatorString
from able import ReaderString

class TestCreatorString(unittest.TestCase):

    def setUp(self):
        self.folder = '{}/Development/Temp/creator_string'.format(os.environ['HOME'])
        self.folder_filename = '{}/creator.txt'.format(self.folder)
        self.contents = 'A=a\nB=b'
        os.makedirs(self.folder, exist_ok=True)
        #with open(self.folder_filename, 'w') as f:
        #    f.write(self.new_contents)

    def tearDown(self):
        fileExists = os.path.isfile(self.folder_filename)
        if fileExists:
            shutil.rmtree(self.folder)

    def test_init(self):
        self.assertTrue(CreatorString(self.folder_filename,self.contents)==self.contents)
        self.assertTrue(os.path.isfile(self.folder_filename))
        self.assertTrue(CreatorString(self.folder_filename,self.contents,hardfail=False)==self.contents)

if __name__ == '__main__':
    unittest.main()