import os
import unittest
import shutil

from able import UpdaterString_NameValueList #UpdaterString, ReaderString

class TestUpdaterString_NameValueList(unittest.TestCase):

    def setUp(self):
        self.nv_list = [{'name': 'A', 'value': 'a'},
                   {'name': 'B', 'value': 'b'},
                   {'name': 'C', 'value': 'c'}]
        self.str_value = "# sample"

    def test_init(self):
        assert(UpdaterString_NameValueList(self.str_value) == self.str_value)
        assert(UpdaterString_NameValueList('# sample').update(self.nv_list) == '# sample\nA=a\nB=b\nC=c')


if __name__ == '__main__':
    unittest.main()