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
        assert (Example().setResult('A', 'github').setResult('B', 'docker').getResult() == {'A': 'github', 'B': 'docker'})
        assert (Example().setResult('A', 'github').getResult('A') == 'github')
        assert (Example().setResult('A', 'github').setResult('B', 'docker').getResult('B') == 'docker')


if __name__ == '__main__':
    unittest.main()