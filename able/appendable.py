
class Appendable():
    ##__Appendable__
    ##
    ## Provide the abilty to append new lines to a document
    ##
    def __init__(self):
        self.appendable=False

    def isAppendable(self):
        ##* get appendable state on request
        return self.appendable
    def setAppendable(self, tf):
        ##* set appendable state on request
        ##
        self.appendable=tf
        return self

def main():
    class Example(Appendable):
        def __init__(self):
            Appendable.__init__(self)

    assert (Example().setAppendable(True).isAppendable())
    assert (not Example().setAppendable(False).isAppendable())

if __name__ == "__main__":
    # execute as docker
    main()