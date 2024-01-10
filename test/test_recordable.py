import unittest
import os
import shutil
from able import Recordable

class TestRecordable(unittest.TestCase):

    def test_init(self):
        class Example(Recordable):
            def __init__(self):
                Recordable.__init__(self)

        expected = {'step_list': [{'msg': '[*] -> A', 'count': 1}, {'msg': '-> B', 'count': 1}]}
        expected_diagram = '[*] -> A -> B'
        assert (Example())
        assert(Recordable().addRecord('A').addRecord('B').getRecording()==expected)
        assert(Recordable().addRecord('A').addRecord('B').getDiagram()==expected_diagram)

if __name__ == '__main__':
    unittest.main()