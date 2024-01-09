import os
import shutil


class Taskable():
    ##
    ##__Taskable__
    ##
    ## Create some legibility for code maintenance
    ##* provide interface for Task
    #def __init__(self):
        #self.fail=False
        #self.msg=[]
        #self.result=None

    def create(self):
        ##* create
        # print('create1')
        return self

    def read(self):
        ##* read
        # print('read1')
        return self

    def update(self):
        ##* update
        # print('update1')
        return self

    def delete(self):
        ##* delete
        # print('delete1')
        return self
    def validateInput(self):
        ##* validate task inputs
        return self

    def validateOutput(self):
        ##* validate task output
        return self


def main():
    # setup

    # test
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


    # tearDown
        # nothing


if __name__ == "__main__":
    # execute as docker
    main()