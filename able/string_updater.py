
class UpdaterString(str):
    ##
    ##__UpdaterString__
    ##
    ## Update with another string
    ##
    def update(self, string_value):
        ##* Update entire string with a new string
        return UpdaterString(string_value)
'''    
class UpdaterString(str):
    ##
    ##__UpdaterString__
    ##
    def update(self, key, new_line):
        ## Replace line containing key with a new line
        ##* eg "A big dog" -> "A big cat"
        key = str(key).strip()

        temp_content = []
        found = False
        for ln in self.split('\n'):
            if key in ln:
                found = True
                temp_content.append(new_line)
            else:
                temp_content.append(ln)
        if not found:
            # insert at end
            temp_content.append(new_line)

        contents = '\n'.join(temp_content)

        return UpdaterString(contents)

    '''


def main():
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
    assert(UpdaterString(str_value).update(new_value) == expected_2)



if __name__ == "__main__":
    # execute as docker
    main()