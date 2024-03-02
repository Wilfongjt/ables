
class ClassNameable():
    ##
    ##__ClassNameable__
    ##
    ## Enable the use of classname for reference
    ##
    def getClassName(self):
        ##* Get Class Name on request
        ##
        return self.__class__.__name__

def main():
    class Example(ClassNameable):
        def __init__(self):
            ClassNameable.__init__(self)

    assert (Example().getClassName()=='Example')

if __name__ == "__main__":
    # execute as docker
    main()