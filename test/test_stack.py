import unittest
import os
import shutil
from able import Stack

class TestStack(unittest.TestCase):

    #def setUp(self):
    #    # setup

    def test_init(self):
        #print('test_init')

        assert (Stack() != None)
        assert (Stack() == [])
        assert (Stack().peek() == None)
        assert (Stack().get(0) == None)
        assert (Stack().get(1) == None)

        #def test_method(self):
        #print('test_method')
        stack = Stack()
        stack.push('model')
        assert (stack == ['model'])
        assert (stack.peek() == 'model')

        stack.push('owner')
        assert (stack == ['model', 'owner'])
        assert (stack.peek() == 'owner')

        stack.push('claim')
        assert (stack == ['model', 'owner', 'claim'])
        assert (stack.peek() == 'claim')

        p = stack.pop()
        assert (stack == ['model', 'owner'])
        assert (stack.peek() == 'owner')
        assert (p == 'claim')

        p = stack.pop()
        assert (stack == ['model'])
        assert (stack.peek() == 'model')
        assert (p == 'owner')

        p = stack.pop()
        assert (stack == [])
        assert (stack.peek() == None)
        assert (p == 'model')

    #def tearDown(self) -> None:
    #    # cleanup
    #    fileExists = os.path.isdir(self.folder)
    #    if fileExists:
    #        shutil.rmtree(self.folder)


if __name__ == '__main__':
    unittest.main()