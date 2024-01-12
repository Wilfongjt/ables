from able.string_updater_namevalue import UpdaterString_NameValue

class NameValueList_UpdaterString(str):
    ##
    ##__NameValueList_UpdaterString__
    ##
    def update(self, nv_list):
        ## Update multiple name-value pairs

        contents = NameValueList_UpdaterString(self)

        for chg in nv_list:
            contents = UpdaterString_NameValue(contents).update(chg['name'], chg['value'])

        return NameValueList_UpdaterString(contents)


def main():
    nv_list = [{'name':'A', 'value': 'a'},
               {'name':'B', 'value': 'b'},
               {'name':'C', 'value': 'c'}]

    assert(NameValueList_UpdaterString('# sample') == '# sample')
    assert(NameValueList_UpdaterString('# sample').update(nv_list) == '# sample\nA=a\nB=b\nC=c')


if __name__ == "__main__":
    # execute as docker
    main()