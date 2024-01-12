import os
import unittest
import shutil
from able.string_updater import UpdaterString

class TestUpdaterString(unittest.TestCase):

    ##__UpdaterString__ Tests

    def setUp(self):
        self.str_value = '''
        #
        # Environment

        '''.replace('  ', '')  # remove leading spaces
        self.expected_1 = self.str_value
        self.new_value = '''
            #
            # File system

            '''.replace('  ', '')  # remove leading spaces
        self.expected_2=self.new_value

    def test_init(self):
        ##*__UpdaterString__ initialization test
        assert (UpdaterString(self.str_value) == self.expected_1)
        ##*__UpdaterString__ update entire string test
        assert (UpdaterString(self.str_value).update(self.new_value) == self.expected_2)
'''
from able import UpdaterString, ReaderString

class TestUpdaterString(unittest.TestCase):

    def setUp(self):

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

'''

if __name__ == '__main__':
    unittest.main()