from able.name_value_pairs import NameValuePairs
from able.matchable import Matchable
class Upsertable():

    def upsert(self, contents, contents_new):
        ## Strategy: evaluate self, one line at a time, to a new string
        # contents has zero or more lines of text
        rc = []
        # convert contents_new string to name-value pairs

        nv_list = NameValuePairs(contents_new)  # convert string to name-value pairs
        # scan self for nv_list line matches
        # if found then update
        # if not found then insert nv_list line
        me = contents.split('\n')
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
                if Matchable().match(ln, search_nm):
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
        return rc

def main():
    contents = ''''''
    assert (Upsertable())
    assert (Upsertable().upsert('A', '') == 'A' )
    assert (Upsertable().upsert('A', 'B') == 'A\nB')
    assert (Upsertable().upsert('A=B', 'A=b') == 'A=b')
    assert (Upsertable().upsert('A=B\nC=c', 'A=b') == 'A=b\nC=c')

if __name__ == "__main__":
    # execute as docker
    main()