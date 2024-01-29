import re

class UpdaterString(str):
    ##
    ##__UpdaterString__
    ##

    ## Update a string with another string
    ##

    def updateAll(self, string_value):
        ##* Update entire string with a new string
        return UpdaterString(string_value)

    def getKey(self, startswith_value):
        ## Create a key from a string
        key = startswith_value
        pattern = re.compile(r'^\s*[A-Z_0-9]+=(.*)$')

        if pattern.match(startswith_value):
            # break up and use [0] as key
            key = '{}='.format(key.split('=')[0])
        return key

    def update(self, startswith_value, new_line_value):
        ## replace a line that starts with a specific value

        key = self.getKey(startswith_value)
        temp_content = []
        found = False
        for ln in self.split('\n'):
            ##* find key and replace with a new line
            if not ln:
                temp_content.append(ln)
            elif ln.strip().startswith(key):
                found = True
                temp_content.append(new_line_value)
            else:
                temp_content.append(ln)
        if not found:
            ##* append when key is not found
            temp_content.append(new_line_value)

        contents = '\n'.join(temp_content)

        return UpdaterString(contents)

    def updates(self, contents_new):
        ## Update multiple name-value pairs

        contents = UpdaterString(self)
        #print('---')
        #print('split', contents_new.split('\n'))
        for ln in contents_new.split('\n'):
            #print('ln',ln)
            if ln:
                contents = contents.update(ln, ln)

        return UpdaterString(contents)


'''
Use Cases
Initialize from a file
Update with a new line
Update with an existing line

## Updater Use Cases
##|        | state                            | op | find startswith | replace line | to | outcome          |
##| ------ | -------------------------------- | -- | --------------- | ------------ | -- | ---------------- |
##| append | []                               | +  | 'abc 123'       | 'abc 123'    | -> | ['abc 123']  |
##| ignore | ['abc 123']                      | +  | 'abc 123'       | 'abc 123'    | -> | ['abc 123']  |
##| update | ['abc 123']                      | +  | 'abc'           | 'abc=123'    | -> | ['abc=123']  |
##| update | ['abc=123']                      | +  | 'abc'           | 'ABC=123'    | -> | ['ABC=123']  |
##| append | ['ABC=123']                      | +  | 'de'            | 'de=xxx'     | -> | ['ABC=123', 'de=xxx']  |

'''

def main():

    # updateAll
    str_value = '''
    #
    # Environment

    '''.replace('  ', '')  # remove leading spaces
    expected_1 = str_value
    new_value = '''
        #
        # File system

        '''.replace('  ', '')  # remove leading spaces

    expected_2=new_value
    assert(UpdaterString(str_value) == expected_1)
    assert(UpdaterString(str_value).updateAll(new_value) == expected_2)

    # update
    str_value = "A=A\nB=B"
    expected1 = "A=a\nB=B"
    expected2 = "A=A\nB=b"
    expected3 = "A=A\nB=B\nC=C"
    assert(UpdaterString(str_value).update('A=', 'A=a') == expected1)
    assert(UpdaterString(str_value).update('B=', 'B=b') == expected2)
    assert(UpdaterString(str_value).update('C=', 'C=C') == expected3)

    # updates
    nv_list = [{'name':'A', 'value': 'a'},
               {'name':'B', 'value': 'b'},
               {'name':'C', 'value': 'c'}]
    list1 = '# sample\nA=a\nB=b\nC=c'
    list2 = '\n# xsample\nD=d\nE=e\nF=f'
    list3 = '# sample\nA=A\nB=B\nC=C'
    #print ('xx', UpdaterString(list1).updates(list2))
    #problem whern second file starts with '\n' '# sample\nA=a\nB=b\nC=c\n# xsample\nD=d\nE=e\nF=f'
    #print('AA','# sample\nA=a\nB=b\nC=c\n# xsample\nD=d\nE=e\nF=f'.replace('\n','.'))
    #print('BB',UpdaterString(list1).updates(list2).replace('\n','.'))
    assert(UpdaterString(list1).updates(list2)=='# sample\nA=a\nB=b\nC=c\n# xsample\nD=d\nE=e\nF=f')
    assert(UpdaterString(list1).updates(list1)=='# sample\nA=a\nB=b\nC=c')
    assert(UpdaterString(list1).updates(list2).updates(list3)=='# sample\nA=A\nB=B\nC=C\n# xsample\nD=d\nE=e\nF=f')


if __name__ == "__main__":
    # execute as docker
    main()
