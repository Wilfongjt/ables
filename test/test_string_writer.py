import os
import unittest
import shutil

from able import StringWriter

class TestStringWriter(unittest.TestCase):

    def setUp(self):
        self.content_string = 'A\nB\nC'
        self.folder = '{}/Development/Temp/string_writer'.format(os.environ['HOME'])
        self.folder_filename = '{}/string_writer.txt'.format(self.folder)

        # setup
        self.content_string = 'A=github\nB=docker'
        os.makedirs(self.folder, exist_ok=True)


    def test_init(self):
        # testapi
        assert (StringWriter(self.folder_filename, self.content_string))
        assert (os.path.isfile(self.folder_filename))

    def tearDown(self):
        fileExists = os.path.isfile(self.folder_filename)
        if fileExists:
            shutil.rmtree(self.folder)

if __name__ == '__main__':
    unittest.main()