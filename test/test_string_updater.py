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
        ##*__UpdaterString__ initialization testapi
        assert (UpdaterString(self.str_value) == self.expected_1)
        ##*__UpdaterString__ update entire string testapi
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

    def test_updates(self):
        d1 = '# 1sample\nA=github'
        d2 = '\n# 2sample\nD=d\n \nE=e'
        d3 = '\n# 3sample\nF=f\n \nF=g'
        assert (UpdaterString(d1) == d1)
        assert (UpdaterString(d2) == d2)
        assert (UpdaterString(d3) == d3)


        m1 = '# m1'
        A = 'A=github'
        B = 'B=docker'
        B1 = 'B=<<bb>>'
        s1 = '{}\n{}\n{}'.format(m1, A, B)
        s2 = '\n# d2\nC=c'
        s3 = '\n# d3\n# another\nD=d'
        s4 = 'A=A\nB=B'
        e1 = s1
        e2 = '\n'.join(s1.split('\n') + s2.split('\n'))
        e3 = '\n'.join(e2.split('\n') + s3.split('\n'))
        e4 = e3.replace(A, 'A=A').replace(B, 'B=B')

        #print('s1', s1.split('\n'))
        #print('s2', s2.split('\n'))
        #print('s3', s3.split('\n'))
        #print('s4', s4.split('\n'))

        #print('e1    ', e1.split('\n'))
        #print('e2    ', e2.split('\n'))
        #print('e3    ', e3.split('\n'))
        #print('e4    ', e4.split('\n'))

        # e4 = '\n'.join(e4)
        assert (UpdaterString(s1) == e1)
        assert (UpdaterString(s1).updates(s2) == e2)
        assert (UpdaterString(s1).updates(s2).updates(s3) == e3)

        #print('e4    ', e4.replace('\n', '|'))
        #print('actual', UpdaterString(s1).updates(s2).updates(s3).replace('\n', '|'))
        assert (UpdaterString(s1).updates(s2).updates(s3).updates(s4) == e4)
        assert (UpdaterString(s1).updates(s2).updates(s3).updates(s4).updates(B1) == e4)


if __name__ == '__main__':
    unittest.main()