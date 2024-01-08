import os
import unittest
import shutil

from able import Appendable

class TestCreatorString(unittest.TestCase):

    def test_init(self):
        class Example(Appendable):
            def __init__(self):
                Appendable.__init__(self)

        assert (Example().setAppendable(True).isAppendable())
        assert (not Example().setAppendable(False).isAppendable())


if __name__ == '__main__':
    unittest.main()