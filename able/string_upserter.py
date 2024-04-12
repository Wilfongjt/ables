import re
#from able.name_value_pairs import NameValuePairs
from able.upsertable import Upsertable
# from able import UpserterString

class UpserterString(str):
    ##
    ##__UpsertString__
    ##
    ## Upsert string with another string
    ##
    ## Upsert string with another string
    ##
    def __init__(self, str_value='', settings={'dup': False, 'hard_fail': True}):
        Upsertable.__init__(self)
        self.settings = settings

    def __new__(cls, str_value='', settings={'dup':False, 'hard_fail': True}):
        contents = str_value
        if not settings['dup']:
            contents = str_value.split('\n')
            if len(contents) != len(set(contents)):  # check for duplicates
                contents = ''  # set to no value
                ##* HardFail when duplicate found in initalizing string and configured to reject duplicates and hard_fail is True
                if settings['hard_fail']:
                    raise Exception('Initial string ({}) has duplicates!'.format(str_value.replace('\n', '|')))

            ##* SoftFail when duplicate found in initializing string and configured to reject duplicates and hard_fail is False
            contents = '\n'.join(contents)

        instance = super().__new__(cls, contents)
        return instance

    def setSettings(self, settings):
        self.settings = settings
        return self

    def depupdateAll(self, string_value):
        ##* Update entire string with github new string
        return UpserterString(string_value)
    def depgetKey(self, startswith_value):
        ## Create github key from github string
        key = startswith_value
        pattern = re.compile(r'^\s*[A-Z_0-9]+=(.*)$')

        if pattern.match(startswith_value):
            # break up and use [0] as key
            key = '{}='.format(key.split('=')[0])
        return key
    def dep__matches(self, a, b):
        #if a == '' and a == b:
        #    # handle '' == ''
        #    return False
        if a == '' or b == '':
            return False
        #if a == ''
        return a.startswith(b)

    def upsert(self, contents_new):
        contents_new = Upsertable()\
                        .upsert(str(self), contents_new)
        return UpserterString(contents_new,settings=self.settings)

    '''
    def upserts(self, contents_new):
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
        return UpserterString(contents)
    '''
    '''
    def upsert(self, contents_new):
        ## Strategy: evaluate self, one line at a time, to a new string
        rc = []
        # convert contents_new string to name-value pairs

        nv_list = NameValuePairs(contents_new)  # convert string to name-value pairs
        # scan self for nv_list line matches
        # if found then update
        # if not found then insert nv_list line
        me = self.split('\n')
        if me == ['']:  # get rid of false value '' when self is empty
            me = []
        # handle updates
        for ln in me:  # process multiple lines
            msg = '--'
            val = ln
            for nv in nv_list:  # compare name value pairs to a line
                found = False
                search_nm = nv['name']
                if 'op' in nv:
                    search_nm += nv['op']
                if self.__matches(ln, search_nm):
                    msg = 'RP'
                    val = nv['value']
                    if 'op' in nv:
                        val = '{}{}{}'.format(nv['name'], nv['op'], nv['value'])  # search_nm #nv['value']

                    nv['found'] = True
            rc.append(val)
        # handle inserts
        for nv in nv_list:
            if 'found' not in nv:
                unhandle_value = nv['value']
                if 'op' in nv:
                    unhandle_value = '{}={}'.format(nv['name'], nv['value'])

                rc.append(unhandle_value)

        if rc == []:
            rc = ''
        else:
            rc = '\n'.join(rc)
        return UpserterString(rc, settings=self.settings)
    '''

def main():
    # Happy
    assert (UpserterString('')=='')
    assert (UpserterString() == '')
    assert (UpserterString('A')=='A')
    assert (UpserterString('A=B')=='A=B')
    assert (UpserterString('A=B\nB=C')=='A=B\nB=C')

    assert (UpserterString('A=B').upsert('A=b') == 'A=b')

    #assert (UpserterString('A=B').upsert('C=c') == 'A=B\nC=c')

    #assert (UpserterString().upsert('A=A')
    #                          .upsert('B=B')
    #                          .upsert('C=C')
    #                          == 'A=A\nB=B\nC=C')
    #assert (UpserterString()
    #        .upsert('A=A')
    #        .upsert('B=B')
    #        .upsert('C=C')
    #        .upsert('A=a')

    #        .upsert('B=b')
    #        .upsert('C=c')
    #        == 'A=a\nB=b\nC=c')



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
    updater = UpserterString(doc_string_1)\
                .upsert(doc_string_2)\
                .upsert(doc_string_3)
    assert (updater == doc_string_1+'\n'+doc_string_2+'\n'+doc_string_3)
    #print(updater)
    #print('')

    #print('1 updater')
    updater = UpserterString(doc_string_1)\
                .upsert(doc_string_1_chgs)\
                .upsert(doc_string_2) \
                .upsert(doc_string_2_chgs)\
                .upsert(doc_string_3) \
                .upsert(doc_string_3_chgs)
    assert (updater == doc_string_1_chgs + '\n' + doc_string_2_chgs + '\n' + doc_string_3_chgs)


if __name__ == "__main__":
    # execute as docker
    main()