from able.string_updater_namevalue import UpdaterString_NameValue

class UpdaterString_NameValueList(str):
    ##
    ##__UpdaterString_NameValueList__
    ##
    def update(self, nv_list):
        ## Update multiple name-value pairs

        contents = UpdaterString_NameValueList(self)

        for chg in nv_list:
            contents = UpdaterString_NameValue(contents).update(chg['name'], chg['value'])

        return UpdaterString_NameValueList(contents)


def main():
    nv_list = [{'name':'A', 'value': 'a'},
               {'name':'B', 'value': 'b'},
               {'name':'C', 'value': 'c'}]

    assert(UpdaterString_NameValueList('# sample') == '# sample')
    assert(UpdaterString_NameValueList('# sample').update(nv_list) == '# sample\nA=a\nB=b\nC=c')


if __name__ == "__main__":
    # execute as docker
    main()