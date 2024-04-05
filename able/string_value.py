class ValueString(str):
    def __new__(cls, str_value='', break_on='='):
        # A -> A
        # A=a -> 'A=a'
        contents = str_value
        '''
        contents = str_value.split(break_on)
        if len(contents)>1:
            contents = '{}'.format(contents[1])
        else:
            contents = contents[0]
        '''
        instance = super().__new__(cls, contents)
        return instance

def main():

    assert(ValueString() == '')
    assert(ValueString('') == '')
    assert(ValueString('A') == 'A')
    assert(ValueString('    A') == '    A')
    assert(ValueString('A=B') == 'A=B')

if __name__ == "__main__":
    # execute as docker
    main()