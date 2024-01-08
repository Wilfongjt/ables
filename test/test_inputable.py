import os
import unittest
import shutil

from able import Inputable

class TestInputable(unittest.TestCase):

    def test_init(self):
        class Example(Inputable):
            def __init__(self):
                Inputable.__init__(self)
        assert (Example())
        #assert (Example().get_input('Hi',default='Bye',hardstop=False)=='Bye')

if __name__ == '__main__':
    unittest.main()