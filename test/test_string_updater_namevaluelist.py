import os
import unittest
import shutil

from able import NameValueList_UpdaterString #UpdaterString, ReaderString

class TestUpdaterString_NameValueList(unittest.TestCase):

    def setUp(self):
        self.nv_list = [{'name': 'A', 'value': 'a'},
                   {'name': 'B', 'value': 'b'},
                   {'name': 'C', 'value': 'c'}]
        self.str_value = "# sample"

    def test_init(self):
        assert(NameValueList_UpdaterString(self.str_value)==self.str_value)
        assert(NameValueList_UpdaterString('# sample').update(self.nv_list) == '# sample\nA=a\nB=b\nC=c')


if __name__ == '__main__':
    unittest.main()