import re


# from able import UpdaterString

class UpdaterString(str):
    ##
    ##__UpdaterString__
    ##

    ## Update github string with another string
    ##

    def __new__(cls, str_value):
        contents = str_value

        instance = super().__new__(cls, contents)
        return instance

    def updateAll(self, string_value):
        ##* Update entire string with github new string
        return UpdaterString(string_value)

    def getKey(self, startswith_value):
        ## Create github key from github string
        key = startswith_value
        pattern = re.compile(r'^\s*[A-Z_0-9]+=(.*)$')

        if pattern.match(startswith_value):
            # break up and use [0] as key
            key = '{}='.format(key.split('=')[0])
        return key

    def updates(self, contents_new):
        # contents_new is a string
        ## Update multiple name-value pairs
        contents = self.split('\n')
        contents_new = contents_new.split('\n')
        # eval incomming text, one line at a time
        for ln in contents_new:
            if ln == '':
                ##* Append empty lines by default
                contents.append(ln)
            elif len(ln) > 0 and len(ln.strip()) == 0:
                ##* Append blank lines by default
                contents.append(ln)
            else:
                ##* Update existing lines
                found = False
                key = self.getKey(ln)
                i = 0
                for r in self.split('\n'):
                    if r.startswith(key):
                        ##* Update existing line with new value

                        found = True
                        if '<<' not in ln:
                            ##* Avoid overwriting user settings when value contains template key
                            contents[i] = ln

                    i += 1
                if not found:
                    ##* insert line when not found
                    contents.append(ln)

        contents = '\n'.join(contents)
        return UpdaterString(contents)

def main():
    doc_string_1 = '''# PROJECT
    WS_ORGANIZATION=<<WS_ORGANIZATION>>
    WS_WORKSPACE=<<WS_WORKSPACE>>'''
    doc_string_1 = '\n'.join([ln.strip() for ln in doc_string_1.split('\n')])

    doc_string_1_chgs = '''# PROJECT
        WS_ORGANIZATION=chg_org
        WS_WORKSPACE=chg_ws'''
    doc_string_1_chgs = '\n'.join([ln.strip() for ln in doc_string_1_chgs.split('\n')])

    doc_string_2 = '''# GitHub
    GH_TRUNK=main
    GH_USER=<<GH_USER>>
    GH_PROJECT=<<GH_PROJECT>>
    GH_BRANCH=<<GH_BRANCH>>
    GH_MESSAGE=first_commit
    GH_TOKEN=<<GH_TOKEN>>'''
    doc_string_2 = '\n'.join([ln.strip() for ln in doc_string_2.split('\n')])

    doc_string_2_chgs = '''# GitHub
    GH_TRUNK=main
    GH_USER=GH_USER
    GH_PROJECT=GH_PROJECT
    GH_BRANCH=GH_BRANCH
    GH_MESSAGE=first_commit
    GH_TOKEN=GH_TOKEN'''
    doc_string_2_chgs = '\n'.join([ln.strip() for ln in doc_string_2_chgs.split('\n')])

    doc_string_3 = '''# NODE_ENV:
    #          production | staging | testapi
    NODE_ENV=development
    # HOST=0.0.0.0
    # PORT=5555'''
    doc_string_3 = '\n'.join([ln.strip() for ln in doc_string_3.split('\n')])

    doc_string_3_chgs = '''# NODE_ENV:
    #          production | staging | testapi
    NODE_ENV=development
    # HOST=0.0.0.0
    # PORT=5555'''
    doc_string_3_chgs = '\n'.join([ln.strip() for ln in doc_string_3_chgs.split('\n')])

    #print('1 updater')
    updater = UpdaterString(doc_string_1).updates(doc_string_2).updates(doc_string_3)
    assert (updater == doc_string_1+'\n'+doc_string_2+'\n'+doc_string_3)
    #print(updater)
    #print('')

    #print('1 updater')
    updater = UpdaterString(doc_string_1)\
                .updates(doc_string_1_chgs)\
                .updates(doc_string_2) \
                .updates(doc_string_2_chgs)\
                .updates(doc_string_3) \
                .updates(doc_string_3_chgs)
    assert (updater == doc_string_1_chgs + '\n' + doc_string_2_chgs + '\n' + doc_string_3_chgs)
    #print(updater)
    #print('')


if __name__ == "__main__":
    # execute as docker
    main()