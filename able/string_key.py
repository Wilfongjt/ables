
class KeyString(str):
    def __new__(cls, str_value='', break_on='='):
        # A -> A
        # A=a -> 'A='

        contents = str_value.split(break_on)
        if len(contents)>1:
            contents = '{}{}'.format(contents[0],break_on)
            #contents = contents[0]
        else:
            contents = contents[0]

        instance = super().__new__(cls, contents)
        return instance

def main():

    assert(KeyString() == '')
    assert(KeyString('') == '')
    assert(KeyString('A') == 'A')
    assert(KeyString('    A') == '    A')
    assert(KeyString('A=B') == 'A=')

if __name__ == "__main__":
    # execute as docker
    main()