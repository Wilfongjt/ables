import os
import unittest
import shutil
from able.string_merger import MergerString

class TestMergerString(unittest.TestCase):

    ##__MergerString__ Tests

    def setUp(self):

        self.t_str = '''
            NAME=<<NAME>>
            DATA=<<DATA>>
        '''.replace('  ', '')  # remove leading spaces

        self.expected_1 = '''
                NAME=<<NAME>>
                DATA=data
                '''.replace('  ', '')
        self.expected_2 = '''
            NAME=name
            DATA=data
            '''.replace('  ', '')

        self.nv_list = [{'name': '<<NAME>>', 'value': 'name'},
                   {'name': '<<DATA>>', 'value': 'data'}]

    def test_init(self):
        ##*__MergerString__ initialization testapi
        assert (MergerString(self.t_str) == self.t_str)

        ##*__MergerString__ update entire string testapi

    def test_imeadiate_templatizationl(self):
        # imeadiate templatization
        assert (MergerString(self.t_str, []) == self.t_str)
        assert(MergerString(self.t_str).merge('<<DATA>>','data')==self.expected_1) # delay templatization
        assert(MergerString(self.t_str).merges(self.nv_list)==self.expected_2) # delay templatization

    def test_delayed_templatization(self):
        # delay templatization
        assert(MergerString(self.t_str, self.nv_list)==self.expected_2) # immeadiate templatization

if __name__ == '__main__':
    unittest.main()