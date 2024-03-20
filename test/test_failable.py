import os
import unittest
import shutil

from able import Failable

class TestFailable(unittest.TestCase):

    def test_init(self):
        class Example(Failable):
            def __init__(self):
                Failable.__init__(self)

        actual = Example()
        assert (actual.setFail('testapi fail 1').isFail())
        assert (actual.setFail('testapi fail 2').getFailMessages()==['testapi fail 1','testapi fail 2'])



if __name__ == '__main__':
    unittest.main()