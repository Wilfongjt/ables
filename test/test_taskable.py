import unittest
import os
import shutil
from able import Taskable

class TestTaskable(unittest.TestCase):


    def test_init(self):
        class Example(list, Taskable):
            def __init__(self):
                Taskable.__init__(self)
            def create(self):
                ##* create
                self.append('create')
                return self

            def read(self):
                ##* read
                self.append('read')
                return self

            def update(self):
                ##* update
                self.append('update')
                return self

            def delete(self):
                ##* delete
                self.append('delete')
                return self

            def validateInput(self):
                ##* validate task inputs
                self.append('validateInput')
                return self

            def validateOutput(self):
                ##* validate task output
                self.append('validateOutput')
                return self

        assert (Example()==[])
        assert (Example().validateInput()==['validateInput'])
        assert (Example().create()==['create'])
        assert (Example().read()==['read'])
        assert (Example().update()==['update'])
        assert (Example().delete()==['delete'])
        assert (Example().validateInput().create().read().update().delete().validateOutput()
                ==['validateInput', 'create', 'read', 'update', 'delete', 'validateOutput'])




if __name__ == '__main__':
    unittest.main()