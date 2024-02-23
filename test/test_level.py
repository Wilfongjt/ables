import os
import unittest
import shutil

from able import Level

class TestLevel(unittest.TestCase):

    # def setUp(self):

    def test_init(self):
        # test
        assert (Level('')==0)
        assert (Level('abc')==0)
        assert (Level('# abc') == 1)
        assert (Level('## abc') == 2)
        assert (Level('### abc') == 3)
        assert (Level('### # abc') == 3)

    #def tearDown(self):
    #    fileExists = os.path.isfile(self.folder_filename)
    #    if fileExists:
    #        shutil.rmtree(self.folder)

if __name__ == '__main__':
    unittest.main()