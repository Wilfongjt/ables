import os
import unittest
import shutil

from able import ClassNameable

class TestClassNameable(unittest.TestCase):

    def test_init(self):
        class Example(ClassNameable):
            def __init__(self):
                ClassNameable.__init__(self)

        assert (Example().getClassName()=='Example')


if __name__ == '__main__':
    unittest.main()