import os
import unittest
import shutil

from able import IsObject

class TestIsObject(unittest.TestCase):

    # def setUp(self):

    def test_init(self):
        # testapi
        assert (not IsObject('abc'))
        assert (IsObject('{abc}'))
        assert (IsObject('{abc: abc, bbb: ccc}'))

        assert (not IsObject('[]'))
        assert (not IsObject('[abc]'))
        assert (not IsObject('[abc,abc]'))

    #def tearDown(self):
    #    fileExists = os.path.isfile(self.folder_filename)
    #    if fileExists:
    #        shutil.rmtree(self.repo_folder)

if __name__ == '__main__':
    unittest.main()