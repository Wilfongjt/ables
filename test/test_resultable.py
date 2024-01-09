import unittest
import os
import shutil
from able import Resultable

class TestResultable(unittest.TestCase):


    def test_init(self):
        class Example(Resultable):
            def __init__(self):
                Resultable.__init__(self)

        assert (Example())
        assert (Example().setResult('A', 'a').setResult('B', 'b').getResult() == {'A': 'a', 'B': 'b'})
        assert (Example().setResult('A', 'a').getResult('A') == 'a')
        assert (Example().setResult('A', 'a').setResult('B', 'b').getResult('B') == 'b')


if __name__ == '__main__':
    unittest.main()