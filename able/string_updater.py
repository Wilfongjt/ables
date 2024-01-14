
class UpdaterString(str):
    ##
    ##__UpdaterString__
    ##

    ## Update with another string
    ##
    #def __init__(self):
    #    self.updated_value = ''

    #def create_instance(self):
    #    return UpdaterString(self.updated_value)

    def updateAll(self, string_value):
        ##* Update entire string with a new string
        return UpdaterString(string_value)

    def update(self, key, value):
        ## Update a single line with a name-value pair
        key = str(key).strip()

        temp_content = []
        found = False
        for ln in self.split('\n'):
            ##* find key and replace with name=value pair
            if ln.strip().startswith(key):
                found = True
                temp_content.append('{}={}'.format(key, value))
            else:
                temp_content.append(ln)
        if not found:
            ##* append when key is not found
            # insert at end
            temp_content.append('{}={}'.format(key, value))

        contents = '\n'.join(temp_content)

        return UpdaterString(contents)

    def updates(self, nv_list):
        ## Update multiple name-value pairs

        contents = UpdaterString(self)

        for chg in nv_list:
            contents = contents.update(chg['name'],chg['value'])

        #contents = '\n'.join(contents)
        return UpdaterString(contents)


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
    assert(UpdaterString(str_value).update('A', 'a') == expected1)
    assert(UpdaterString(str_value).update('B', 'b') == expected2)
    assert(UpdaterString(str_value).update('C', 'C') == expected3)

    # updates
    nv_list = [{'name':'A', 'value': 'a'},
               {'name':'B', 'value': 'b'},
               {'name':'C', 'value': 'c'}]
    #print('updates', UpdaterString('# sample').updates(nv_list))
    assert(UpdaterString('# sample').updates(nv_list) == '# sample\nA=a\nB=b\nC=c')
    assert(UpdaterString('# sample\nA=A').updates(nv_list) == '# sample\nA=a\nB=b\nC=c')
    assert(UpdaterString('# sample\nA=A\nB=B').updates(nv_list) == '# sample\nA=a\nB=b\nC=c')

if __name__ == "__main__":
    # execute as docker
    main()