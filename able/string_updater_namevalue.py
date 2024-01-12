from able.string_updater import UpdaterString

class UpdaterString_NameValue(UpdaterString):
    ##
    ##__NameValue_UpdaterString__
    ##
    #def __new__(cls, string_value):
    #    instance = super().__new__(cls, contents)
    #    return instance

    def update(self, key, value):
        ## Update a single line with a name-value pair
        #print('key: {} value: {}'.format(key, value))
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

        return UpdaterString_NameValue(contents)

def main():
    str_value = "A=A\nB=B"
    expected1 = "A=a\nB=B"
    expected2 = "A=A\nB=b"
    expected3 = "A=A\nB=B\nC=C"

    assert(UpdaterString_NameValue(str_value))
    assert(UpdaterString_NameValue(str_value).update('A', 'a') == expected1)
    assert(UpdaterString_NameValue(str_value).update('B', 'b') == expected2)
    assert(UpdaterString_NameValue(str_value).update('C', 'C') == expected3)


if __name__ == "__main__":
    # execute as docker
    main()