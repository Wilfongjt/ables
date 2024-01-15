import os
import unittest
import shutil
from able.string_template import TemplateString

class TestTemplateString(unittest.TestCase):

    ##__TemplateString__ Tests

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
        ##*__TemplateString__ initialization test
        assert (TemplateString(self.t_str) == self.t_str)

        ##*__TemplateString__ update entire string test

    def test_imeadiate_templatizationl(self):
        # imeadiate templatization
        assert (TemplateString(self.t_str, []) == self.t_str)
        assert(TemplateString(self.t_str).merge('<<DATA>>','data')==self.expected_1) # delay templatization
        assert(TemplateString(self.t_str).merges(self.nv_list)==self.expected_2) # delay templatization

    def test_delayed_templatization(self):
        # delay templatization
        assert(TemplateString(self.t_str, self.nv_list)==self.expected_2) # immeadiate templatization

if __name__ == '__main__':
    unittest.main()