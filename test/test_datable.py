import os
import unittest
import shutil

from able import Datable

class TestDatable(unittest.TestCase):
    def setUp(self) -> None:
        # setup
        self.data = [{'name': 'A', 'value': 'github'}, {'name': 'B', 'value': 'docker'}]

    def test_init(self):
        class Example(Datable):
            def __init__(self):
                Datable.__init__(self)

        assert (Example().setData(self.data).getData() == self.data)
        assert (Example().setData(self.data).getData('B') == 'docker')
        assert (Example().setData(self.data).getData('A') == 'github')

    #def tearDown(self) -> None:
    #    # tearDown


if __name__ == '__main__':
    unittest.main()