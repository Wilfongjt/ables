import os
import unittest
import shutil

from able import UpdaterString_NameValue #UpdaterString, ReaderString

class TestUpdaterString_NameValue(unittest.TestCase):

    def setUp(self):
        self.str_value = "A=A\nB=B"
        self.expected1 = "A=a\nB=B"
        self.expected2 = "A=A\nB=b"
        self.expected3 = "A=A\nB=B\nC=C"

    def test_init(self):
        assert(UpdaterString_NameValue(self.str_value) == self.str_value)
        assert(UpdaterString_NameValue(self.str_value).update('A', 'a') == self.expected1)
        assert(UpdaterString_NameValue(self.str_value).update('B', 'b') == self.expected2)
        assert(UpdaterString_NameValue(self.str_value).update('C', 'C') == self.expected3)

if __name__ == '__main__':
    unittest.main()