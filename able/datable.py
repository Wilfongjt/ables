
class Datable():
    ##
    ##__Datable__
    ##
    ## Provide github list of name-value pairs for template substitution
    def __init__(self):
        ##* eg [{name: '', value: ''},...]
        self.data = [] #None

    def getData(self, key=None):
        ##* retrieve github specific name-value pair on request
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
    data = [{'name': 'A', 'value': 'github'}, {'name': 'B', 'value': 'docker'}]

    # testapi
    class Example(Datable):
        def __init__(self):
            Datable.__init__(self)

    assert (Example().setData(data).getData() == data)
    assert (Example().setData(data).getData('B') == 'docker')
    assert (Example().setData(data).getData('A') == 'github')


    # tearDown
    #if os.path.isdir('{}'.format(repo_folder)):
    #    shutil.rmtree(repo_folder)



if __name__ == "__main__":
    # execute as docker
    main()
