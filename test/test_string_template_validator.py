import os
import unittest
import shutil
from able.string_template_validator import TemplateStringValidator

class TestTemplateStringValidator(unittest.TestCase):

    ##__TemplateStringValidator__ Tests

    def setUp(self):
        self.tmpl_str = 'abc abc'
        self.tmpl_str2 = 'abc <<A>> <<B>>'

    def test_init(self):
        ##*__TemplateStringValidator__ happy test
        self.assertTrue (TemplateStringValidator(self.tmpl_str) == self.tmpl_str)

        ##*__TemplateStringValidator__  unsub keys test
        with self.assertRaises(Exception):
            TemplateStringValidator(self.tmpl_str2)


if __name__ == '__main__':
    unittest.main()