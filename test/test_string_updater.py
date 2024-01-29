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
    def test_updateAll(self):
        # updateAll
        str_value = '''
        #
        # Environment

        '''.replace('  ', '')  # remove leading spaces
        expected_1 = str_value
        new_value = '''
            #
            # File system

            '''.replace('  ', '')  # remove leading spaces
        expected_2 = new_value
        assert (UpdaterString(str_value) == expected_1)
        assert (UpdaterString(self.str_value).updateAll(self.new_value) == self.expected_2)

    def test_update(self):
        # update
        str_value = "A=A\nB=B"
        expected1 = "A=a\nB=B"
        expected2 = "A=A\nB=b"
        expected3 = "A=A\nB=B\nC=C"
        assert (UpdaterString(str_value).update('A=', 'A=a') == expected1)
        assert (UpdaterString(str_value).update('B=', 'B=b') == expected2)
        assert (UpdaterString(str_value).update('C=', 'C=C') == expected3)

    def test_updates(self):

        # updates
        nv_list = [{'name':'A', 'value': 'a'},
                   {'name':'B', 'value': 'b'},
                   {'name':'C', 'value': 'c'}]
        list1 = '# sample\nA=a\nB=b\nC=c'
        list2 = '\n# xsample\nD=d\nE=e\nF=f'
        list3 = '# sample\nA=A\nB=B\nC=C'

        assert(UpdaterString(list1).updates(list2)=='# sample\nA=a\nB=b\nC=c\n# xsample\nD=d\nE=e\nF=f')
        assert(UpdaterString(list1).updates(list1)=='# sample\nA=a\nB=b\nC=c')
        assert(UpdaterString(list1).updates(list2).updates(list3)=='# sample\nA=A\nB=B\nC=C\n# xsample\nD=d\nE=e\nF=f')

if __name__ == '__main__':
    unittest.main()