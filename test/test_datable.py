import os
import unittest
import shutil

from able import Datable

class TestDatable(unittest.TestCase):
    def setUp(self) -> None:
        # setup
        self.data = [{'name': 'A', 'value': 'a'}, {'name': 'B', 'value': 'b'}]

    def test_init(self):
        class Example(Datable):
            def __init__(self):
                Datable.__init__(self)

        assert (Example().setData(self.data).getData() == self.data)
        assert (Example().setData(self.data).getData('B') == 'b')
        assert (Example().setData(self.data).getData('A') == 'a')

    #def tearDown(self) -> None:
    #    # tearDown


if __name__ == '__main__':
    unittest.main()