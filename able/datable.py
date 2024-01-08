
class Datable():
    ##
    ##__Datable__
    ##
    ## Provide a list of name-value pairs for template substitution
    def __init__(self):
        ##* eg [{name: '', value: ''},...]
        self.data = [] #None

    def getData(self, key=None):
        ##* retrieve a specific name-value pair on request
        if key:
            for d in self.data:
                if key == d['name']:
                    return d['value']

        ##* retrieve all name-value pairs on request
        return self.data

    def setData(self, nv_list):
        ##* set name-value pairs on request
        self.data = nv_list
        return self

def main():
    # setup
    data = [{'name': 'A', 'value': 'a'}, {'name': 'B', 'value': 'b'}]

    # test
    class Example(Datable):
        def __init__(self):
            Datable.__init__(self)

    assert (Example().setData(data).getData() == data)
    assert (Example().setData(data).getData('B') == 'b')
    assert (Example().setData(data).getData('A') == 'a')


    # tearDown
    #if os.path.isdir('{}'.format(folder)):
    #    shutil.rmtree(folder)



if __name__ == "__main__":
    # execute as docker
    main()
