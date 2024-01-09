
class Resultable():
    ##
    ##__Resultable__
    ## provide ablity to store results when needed
    def __init__(self):
        ##* provide dictionary of results
        self.results = {}

    def getResult(self, key=None):
        ##* retrieve specific result on request
        if key:
            return self.results[key]
        ##* retrieve all results on reauest
        return self.results

    def setResult(self, key, value):
        ## set result value by key
        self.results[key]=value
        return self

def main():

    class Example(Resultable):
        def __init__(self):
            Resultable.__init__(self)

    assert (Example())
    assert (Example().setResult('A','a').setResult('B','b').getResult()=={'A': 'a', 'B': 'b'})
    assert (Example().setResult('A','a').getResult('A')=='a')
    assert (Example().setResult('A','a').setResult('B','b').getResult('B')=='b')

if __name__ == "__main__":
    # execute as docker
    main()
