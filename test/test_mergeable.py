import os
import unittest
import shutil

from able import Mergeable

class TestMergeable(unittest.TestCase):

    def setUp(self) -> None:
        # setup
        self.template = 'Hi from <<A>>, looking at <<B>>.'
        self.nv_list = [{'name': '<<A>>', 'value': 'a'}, {'name': '<<B>>', 'value': 'b'}]

    def test_init(self):
        class Example(Mergeable):
            def __init__(self):
                Mergeable.__init__(self)

        assert (Example().merge(self.template, self.nv_list)=='Hi from a, looking at b.')


if __name__ == '__main__':
    unittest.main()