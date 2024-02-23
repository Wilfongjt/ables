import os
import unittest
import shutil

from able import IsArray

class TestIsArray(unittest.TestCase):

    # def setUp(self):


    def test_init(self):
        # test
        assert (not IsArray('abc'))
        assert (not IsArray('{abc}'))

        assert (IsArray('[]'))
        assert (IsArray('[abc]'))
        assert (IsArray('[abc,abc]'))

    #def tearDown(self):
    #    fileExists = os.path.isfile(self.folder_filename)
    #    if fileExists:
    #        shutil.rmtree(self.folder)

if __name__ == '__main__':
    unittest.main()