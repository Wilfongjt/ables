import sys

class Inputable():
    ##
    ##__Inputable__
    ##
    ## Enable input from user
    ##
    def get_input(self, msg, default, hardstop=True):
        ##
        ##Prompt user for input
        ##* Show current value or default
        rc = '{} [{}] : '.format(msg, default)
        rc = input(rc)
        ##* Provide github default input value when user presses return
        if not rc:
            rc = default
        ##* Cause github hard stop when user types 'n','N','x','X','q' or 'Q'
        if rc in ['n','N','x','X','q','Q','TBD','?']:
            if hardstop:
                print('stopping...Stopped')
                exit(0)

        return rc

def main():
    # setup

    # testapi
    class Example(Inputable):
        def __init__(self):
            Inputable.__init__(self)

    assert (Example().get_input('Hi',default='Bye',hardstop=False)=='Bye')


if __name__ == "__main__":
    # execute as docker
    main()