from able.name_value_pairs import NameValuePairs
from able.string_key import KeyString
# settings {'dup': True}
# Insert means append new-line to the end when settings {'dup': True}
# Update means find and replace all found lines settings {'dup': True}
# Upsert means find and replace all found lines otherwise append new-line settings {'dup': True}
# Delete means find and remove all line found lines settings {'dup': True}

# settings {'dup': False}
# Insert means append new-line to the end when new-line not found
# Update means find and replace first found line
# Upsert means find and replace first found line otherwise append new-line
# Delete means find and remove single found

class DataString(str):
    def __init__(self, str_value='', settings={'dup':False, 'hard_fail': True}):
        self.settings=settings

    def __new__(cls, str_value='', settings={'dup':False, 'hard_fail': True}):
        contents = str_value
        #print('---')
        #print('datastring 1 "{}"'.format(contents.replace('\n','|')))
        if not settings['dup']:
            #print('datastring 2')
            contents = str_value.split('\n')
            if len(contents) != len(set(contents)): # check for duplicates
                #print('datastring 3')
                contents = '' # set to no value
                ##* HardFail when duplicate found in initalizing string and configured to reject duplicates and hard_fail is True
                if settings['hard_fail']:
                    raise Exception('Initial string ({}) has duplicates!'.format(str_value.replace('\n','|')))

            ##* SoftFail when duplicate found in initializing string and configured to reject duplicates and hard_fail is False
            contents = '\n'.join(contents)
        #print('datastring 5',contents.replace('\n','|'))
        #contents = str_value
        instance = super().__new__(cls, contents)
        #print('duplicates', len(contents.split('\n')) != len(set(items)))
        #print('datastring out', instance)
        return instance
    '''
        def __new__(cls, str_value='', settings={'dup':False, 'hard_fail': True}):
        contents = str_value
        
        instance = super().__new__(cls, contents)
        print('duplicates', len(contents.split('\n')) != len(set(items)))
        return instance
    '''

    def show(self, label=''):
        print('show', label, self)

        return self

    def getSettings(self):
        return self.settings

    def setHardFail(self, tf):
        self.settings['hard_fail']=tf
        return self
    def isHardFail(self):
        return self.settings['hard_fail']

    def setDuplicate(self, tf):
        self.settings['dup']=tf
        return self

    def allowDuplicate(self):
        return self.settings['dup']
    '''
    def __append(self, line):
        # append line string without dup check
        # use insert for checking

        if len(self) > 0:
            rc = DataString(self + '\n' + line, self.settings)
        else:
            rc = DataString(line, self.settings)

        return rc
    '''
    def __matches(self, a, b):
        #if a == '' and a == b:
        #    # handle '' == ''
        #    return False
        if a == '' or b == '':
            return False
        #if a == ''
        return a.startswith(b)

    def __find(self, line):
        found = False
        i = 0
        for ln in self.split('\n'):
            if self.__matches(ln, line):
                found = {'at': i, 'searching': line}
                break
            i += 1
        return found

    #def __validate(self):

    def delete(self, existing_line):
        # Delete means find and remove a line when settings {'dup': False}
        # Delete means find and remove found lines when settings {'dup': True}
        #print('1 delete existing_line "{}"'.format(existing_line))
        #print('1 delete ', self.replace('\n','|'))
        # Filter out all found lines
        #print('1.1 delete split', self.split('\n'))
        keepers = [ln for ln in self.split('\n') if not self.__matches(ln, existing_line)]
        # reassemble lines into string
        #print('2 delete ', keepers)
        keepers = '\n'.join(keepers)
        #print('3 delete out  keepers',keepers)
        return DataString(keepers,self.getSettings())

    def insert(self, new_line_string):
        # nv_list is [{'name': '', 'value':''}...]
        # Insert means append new-line to the end when new-line not found when settings {'dup': False}
        # Insert means append new-line to the end when settings {'dup': True}
        # eg DataString('somestring').insert(NameValuePairs(StringReader(some_file_path)))

        nv_list = NameValuePairs(new_line_string) # convert string to name-value pairs
        rc = []
        # convert contents into list
        rc = self.split('\n')
        if rc == ['']:
            rc == []
        # print('split rc', rc)

        for nv in nv_list:
            new_line = nv['value']
            rc.append(new_line)

            if not self.allowDuplicate():
                if len(rc) != len(set(rc)): # test for duplicates
                    rc.pop()

        # reassemble lines into string
        rc = '\n'.join(rc)
        # remove leading newlines
        rc = rc.strip()
        return DataString(rc,self.getSettings())

    '''
        def insert(self, new_line_string):
        # nv_list is [{'name': '', 'value':''}...]
        # Insert means append new-line to the end when new-line not found when settings {'dup': False}
        # Insert means append new-line to the end when settings {'dup': True}
        # eg DataString('somestring').insert(NameValuePairs(StringReader(some_file_path)))

        nv_list = NameValuePairs(new_line_string) # convert string to name-value pairs
        rc = []
        for nv in nv_list:
            new_line = nv['value']
            if not self.allowDuplicate(): # no dups
                # make sure new_line is unique
                found = self.__find(new_line) # search for duplicate
                # ignore insert when duplicate found
                if found:
                    found['failed']: 'duplicate'
                    self.settings['failed']=found
                    if self.settings['hard_fail']:
                        raise Exception('Found Duplicate line "{}"'.format(found))
                    return self # avoid appending a duplicate line

            if len(self)==0:
                rc.append(new_line)
            else:
                rc = self.split('\n')
                rc.append(new_line)
            #else:
            #    # add line to end without regard to duplicates
            #    print('5 insert new_line', new_line)
            #    rc = self.split('\n').append(new_line)
            #    #rc = self.__append(new_line)

        # reassemble lines into string
        rc = '\n'.join(rc)
        return DataString(rc,self.getSettings())
    '''
    '''
    
    def insert(self, new_line):
        # Insert means append new-line to the end when new-line not found when settings {'dup': False}
        # Insert means append new-line to the end when settings {'dup': True}
        # eg DataString('somestring').insert(NameValuePairs(StringReader(some_file_path)))

        rc = None
        if not self.allowDuplicate(): # no dups
            # make sure new_line is unique
            found = self.__find(new_line) # search for duplicate
            if found:
                found['failed']: 'duplicate'
                self.settings['failed']=found
                if self.settings['hard_fail']:
                    raise Exception('Found Duplicate line "{}"'.format(found))
                return self # avoid appending a duplicate line
            rc = self.__append(new_line)
        else:
            # add line to end without regard to duplicates
            rc = self.__append(new_line)

        return rc
    '''

    def updateEQ(self, with_line_string):
        # strategy: copy current string line by line to new string, updating lines as found

        #print('-')
        #print('  1 update with', with_line_string.replace('\n', '|'))
        #print('  2 update', self.replace('\n','|'))
        # update
        # given 'A=A\nB=B' eg DataString('A=A\nB=B') == 'A=A\nB=B'.updateEQ('A=a\nA=b')
        # apply 'A=a\nA=b' eg DataString('# com\nA=A\nB=B\n# comm').updateEQ('A=a\nA=b') == '# com\nA=a\nB=b\n# comm'
        # transform ''

        # Break out the '.=.' pattern out from with_line_string
        # 'A=1'
        #
        # use case: DataString().update(set='A=',to='A=1')  -> ''
        # return list
        # use case: DataString().update('')  -> ''
        # use case: DataString().update(A=A) -> ''
        # use case: DataString().update(A=B) -> ''
        # use case: DataString(A=A).update('')  -> A=A
        # use case: DataString(A=A).update(A=A) -> A=A
        # use case: DataString(A=A).update(A=B) -> A=B
        # return DataString(final_content_list, self.getSettings())

        #if self.strip() == '':
        #    print('  A update actual',self.replace('\n','|'))
        #    return self

        rc = []
        # convert string to name-value pairs

        nv_list = NameValuePairs(with_line_string) # convert string to name-value pairs

        i = 0
        # move
        #print(self.split('\n'))
        for ln in self.split('\n'):
            #print(ln)
            msg='--'
            val=ln
            #print('    ln {}:'.format(i), end='')
            for nv in nv_list:
                #print('updateEQ    nv', nv, ln.replace('\n','|'))
                if self.__matches(ln, nv['name']):
                    msg='RP'
                    val=nv['value']
                    #rc.append(nv['value'])
            rc.append(val)
            #print('  {}: {}'.format(msg, val))
            i+=1

        # convert back to string
        #print('rc', rc)

        if rc == []:
            rc = ''
        else:
            rc = '\n'.join(rc)
        #print('rc', rc.replace('\n','|'))
        #print('  B update actual', DataString(rc, self.getSettings()))
        return DataString(rc, self.getSettings())

    def update2dep(self, update_line_string):
        # use case: DataString(A=A).update('')  -> A=A
        # use case: DataString(A=A).update(A=A) -> A=A
        # use case: DataString(A=A).update(A=B) -> A=B

        print('1 update')
        # nv_list is [{'name': '', 'value':''}...]
        # eg DataString('somestring').update(NameValuePairs(StringReader(some_file_path)))
        #
        # Update means find and replace first found line when settings {'dup': False}
        # Update means find and replace all found lines when settings {'dup': True}
        nv_list = NameValuePairs(update_line_string) # convert string to name-value pairs

        if nv_list == []:
            return self

        i = 0
        # split content once
        # update a copy, before commiting
        final_content_list = self.split('\n')
        print('2 update nv_list', nv_list)

        # expect to process multiple name-value pairs eg [{name:'',value:''},{name:'',value:''}]
        print('3 update nv_list', nv_list)
        for item in nv_list:
            print('4 update item', item)
            # name the nv pair item for readability
            existing_line = item['name']
            new_line = item['value']

            print('5 update final_content_list',final_content_list)
            for ln in final_content_list:
                print('5.1 update ln', ln)

                if self.__matches(ln, existing_line):
                    print('matched ({}) and ({})'.format(ln, existing_line))
                    if self.allowDuplicate():
                        # update all when matched
                        final_content_list[i] = new_line
                        updated = True
                    else:  # not dup
                        # only update the first
                        final_content_list[i] = new_line
                        break

                i += 1
        print('6 update')
        # fail all updates if one duplicate is found
        if not self.allowDuplicate() and len(final_content_list) != len(set(final_content_list)):
            print('7 update')
            # stop update when update will cause a duplicate line to be added
            if self.isHardFail():
                print('7.1 update')
                raise Exception('Update will cause Duplicate line ({})'.format(new_line))
            return self # return the unalterd original
        print('8 update')
        final_content_list = '\n'.join(final_content_list)
        print('out update final_content_list', final_content_list)
        return DataString(final_content_list, self.getSettings())

    '''
    def update(self, existing_line, new_line):
        i = 0

        if not self.allowDuplicate() and existing_line==new_line:
            # avoid this pointless update
            return self

        rc = self.split('\n')
        if not self.allowDuplicate() and new_line in rc:
            # stop update when update will cause a duplicate line to be added
            return self

        #print('update', self)

        for ln in rc:

            if self.__matches(ln, existing_line):
                #print('matched ({}) and ({})'.format(ln, existing_line))
                if self.allowDuplicate():
                    # update all when matched
                    rc[i] = new_line
                    updated = True
                else: # not dup
                    rc[i] = new_line
                    break # only update the first

            i += 1
        rc = '\n'.join(rc)
        return DataString(rc, self.getSettings())
    '''
    def upsert(self, existing_line, new_line):
        # Upsert means find and replace first found line otherwise append new-line when settings {'dup': False}
        # Upsert means find and replace all found lines otherwise append new-line when settings {'dup': True}

        # print('-- upsert')
        i = 0

        #if not self.allowDuplicate() and existing_line==new_line:
        #    # avoid this pointless update
        #    print('1 upsert ', self.replace('\n','|'))
        #    return self

        rc = self.split('\n')

        if not self.allowDuplicate() and new_line in rc:
            # stop update when update will cause a duplicate line to be added
            #print('  2 upsert ', self.replace('\n','|'))
            return self
        #print('rc 1', rc)
        #print('update', self)
        if rc==['']:
            # print('  3 upsert ', self.replace('\n','|'))
            return DataString(new_line, self.getSettings())

        updated = False

        for ln in rc:
            # print('rc 2', i, rc)

            if self.__matches(ln, existing_line):
                # print('matched ({}) and ({})'.format(ln, existing_line))
                if self.allowDuplicate():
                    # update all when as found
                    ##* update line when found
                    rc[i] = new_line
                    updated = True
                    # print('rc 3', i, ln, rc)

                else: # not dup
                    ##* update first when no dups and found
                    rc[i] = new_line
                    updated = True
                    # print('ln ({}) existing_line ({})'.format(ln, existing_line))
                    # print('rc 4', i, ln, rc)

                    break # only update the first

            i += 1
        # print('rc 5', i, rc)

        if not updated:
            ##* append line when not found
            rc.append(new_line)

        #print('rc 6', i,rc)

        rc = '\n'.join(rc)
        # print('  4 upsert ', rc.replace('\n', '|'))

        return DataString(rc, self.getSettings())
    '''
    given "", upsert(A) goes to A
    given A, upsert(A) goes to A
    given A, upsert(B) goes to A|B
    given A, upsert(A=B) goes to A=B
    given A|B, upsert(A=B) goes to A=B|B
    given A=B|B, upsert(B=1) goes to A=B|B=1
    
    '''
    def upsertEQ(self, with_line_string):
        # strategy: copy current string line by line to new string, updating lines as found
        #
        # print('*')
        # print('1 DS({}).upsertEQ({}) '.format(self.replace('\n','|'), with_line_string))
        rc = []
        # convert string to name-value pairs

        nv_list = NameValuePairs(with_line_string) # convert string to name-value pairs
        # print('2 upsertEQ {} -> nv_list {}'.format(with_line_string, nv_list))

        i = 0
        # move
        ## print(self.split('\n'))
        found = False

        me = self.split('\n')
        if me == ['']: # get rid of false value '' when self is empty
            me = []
        # print('2.1 upsertEQ me', me)
        for ln in me: # process multiple lines
            ## print(ln)
            msg='--'
            val=ln
            # print('2.1 upsertEQ ln "{}"'.format(ln))
            for nv in nv_list: # compare name value pairs to a line
                ## print('updateEQ    nv', nv, ln.replace('\n','|'))
                search_nm = nv['name']
                if 'op' in nv:
                    search_nm += nv['op']
                ## print('    match({}, {})'.format(ln, search_nm))
                if self.__matches(ln, search_nm):
                    # print('2.1.1 matched ln "{}".startswith({})'.format( ln, search_nm))
                    msg='RP'
                    # print('val={}'.format('{}={}'.format(nv['name'],nv['value'])))
                    val = nv['value']
                    if 'op' in nv:
                        val= '{}{}{}'.format(nv['name'], nv['op'], nv['value']) #search_nm #nv['value']

                    nv['found'] = True
                    #rc.append(nv['value'])
            rc.append(val)
            ## print('  {}: {}'.format(msg, val))
            i+=1
        ## print('3 upsertEQ nv_list', nv_list)
        # print('3 upsertEQ rc', rc)

        # evaluate name value pairs that were not matched and add
        for nv in nv_list:
            if 'found' not in nv:
                # print('3.1 upsertEQ nv',nv)
                unhandle_value = nv['value']
                if 'op' in nv:
                    unhandle_value='{}={}'.format(nv['name'], nv['value'])

                rc.append(unhandle_value)
                #rc.append(nv['value'])

        # convert back to string
        #print('rc', rc)
        # print('4 upsertEQ rc', rc)

        if rc == []:
            rc = ''
        else:
            rc = '\n'.join(rc)
        # print('5 upsertEQ rc', rc.replace('\n','|'))

        #print('rc', rc.replace('\n','|'))
        #print('  B update actual', DataString(rc, self.getSettings()))
        return DataString(rc, self.getSettings())


def test_data_string_init():
    assert (DataString() == '')
    assert (DataString('') == '')
    assert (DataString('A line') == 'A line')
    assert (DataString('A=line') == 'A=line')

def test_data_string_delete():
    # delete

    assert (DataString().delete('') == '')
    assert (DataString().delete('A line') == '')
    assert (DataString('A line').delete('B line') == 'A line')

    assert (DataString('A line').delete('A line') == '')

    #print('---')
    assert(DataString('A line\nB line')
           .setHardFail(False)
           .delete('A line') == 'B line')
    #print('---')

    assert(DataString('A line\nB line')
           .setHardFail(False)
           .delete('B line') == 'A line')

def test_data_string_insert():
    # insert
    #print('insert', DataString()
    #       .setHardFail(False)
    #       .insert('A line'))

    assert(DataString()
           .setHardFail(False)
           .setDuplicate(False)
           .insert('A line')=='A line')
    assert(DataString()
           .setHardFail(False)
           .insert('A line')
           .insert('A line') == 'A line')
    assert(DataString()
           .setHardFail(False)
           .insert('A line')
           .insert('B line') == 'A line\nB line')
    #print(DataString()
    #       .setHardFail(False)
    #       .insert('A line\nB line'))
    assert(DataString()
           .setHardFail(False)
           .insert('A line\nB line') == 'A line\nB line')

def test_data_string_updateEQ():
    # update dup=False
    # DONT USE A>>>>B replace line A with line B
    # A==B set 'A=*' to 'A=B'
    empty = ''''''
    start_string = '''# abc\nA big red fox\nA=A\nB=B\nC=C\n# def''' #.replace('    ', '')#.replace('\n', '|')
    nomatches_string = '''NN=0\nMM=1\nOO=3''' #.replace('    ', '')
    #repl_string = '''A=1\nB=2\nC=3''' #.replace('    ', '')

    exepected_string = '''# abc\nA big red fox\nA=1\nB=2\nC=3\n# def'''

    #print('A', start_string.replace('\n','|'))
    #exit(0)
    # empty tests
    assert (DataString()
            .setHardFail(False)
            .updateEQ(empty)==empty)

    assert (DataString()
            .setHardFail(False)
            .updateEQ(nomatches_string) == empty)

    assert (DataString('A\nB')
            .setHardFail(False)
            .updateEQ('A') == 'A\nB')
            #.update([{'name': 'A', 'value': 'A'}]) == 'A\nB')

    #print('---')
    assert (DataString('A\nB')
            .setHardFail(False)
            .setDuplicate(False)
            .updateEQ('A\nB') == 'A\nB')

    #print ('upsert -',DataString('# abc\nA big red fox\nA=A\nB=B\nC=C\n# def')
    #        .setHardFail(False)
    #        .setDuplicate(False).updateEQ('A=1\nB=2\nC=3')
    #         )

    assert (DataString('# abc\nA big red fox\nA=A\nB=B\nC=C\n# def')
            .setHardFail(False)
            .setDuplicate(False)
            .updateEQ('A=1\nB=2\nC=3') == '# abc\nA big red fox\nA=1\nB=2\nC=3\n# def')

def test_data_string_upsert():
    # Upsert

    assert (DataString()
            .setHardFail(False)
            .upsert('', '') == '')

    #print("B upsert given '' replace '' with A  -> A")

    assert (DataString()
            .setHardFail(False)
            .upsert('', 'A')=='A')

    #print("C upsert given A  replace A  with A  -> A")

    assert (DataString('A')
            .setHardFail(False)
            .upsert('A', 'A')=='A')

    #print("D upsert given AB replace A  with B  -> AB")

    assert (DataString('A\nB')
            .setHardFail(False)
            .upsert('A', 'B')=='A\nB')

    #print("E upsert given AB replace A  with C  -> CB")

    assert (DataString('A\nB')
            .setHardFail(False)
            .upsert('A', 'C')=='C\nB')

    #print("F upsert given AB replace B  with C  -> AC")

    assert (DataString('A\nB')
            .setHardFail(False)
            .upsert('B', 'C') == 'A\nC')

    #print("G upsert given AB replace '' with C  -> AB")

    assert (DataString('A\nB')
          .setHardFail(False)
          .upsert('', 'C')=='A\nB\nC')

    #print("H upsert given AB replace C  with C  -> ABC")

    assert (DataString('A\nB')
          .setHardFail(False)
          .upsert('C', 'C') == 'A\nB\nC')


def test_data_string_upsertEQ():
    # Upsert
    #     given "", upsert("") goes to ""
    #     given "", upsert(A) goes to A
    #     given A, upsert(A) goes to A
    #     given A, upsert(B) goes to A|B
    #     given A, upsert(A=B) goes to A=B
    #     given A|B, upsert(A=B) goes to A=B|B
    #     given A=B|B, upsert(B=1) goes to A=B|B=1

    # given "", upsert("") goes to ""
    assert (DataString()
            .setHardFail(False)
            .upsertEQ('') == '')

    #print("B upsert given '' replace '' with A  -> A")

    # given "", upsert(A) goes to A

    assert (DataString()
            .setHardFail(False)
            .upsertEQ('A') == 'A')

    # given A, upsert(A) goes to A
    #print('--  given A, upsert(A) goes to A')
    assert (DataString('A')
            .setHardFail(False)
            .upsertEQ('A') == 'A')

    #     given A, upsert(B) goes to A|B

    assert (DataString('A')
            .setHardFail(False)
            .upsertEQ('B')
            == 'A\nB')

    #     given A, upsert(A=B) goes to A=B

    assert (DataString('A')
            .setHardFail(False)
            .upsertEQ('A=B')
            == 'A\nA=B')

    #     given A|B, upsert(A=B) goes to A=B|B
    assert (DataString('A\nB')
            .setHardFail(False)
            .upsertEQ('A=B')
            == 'A\nB\nA=B')
    #     given A=B|B, upsert(B=1) goes to A=B|B=1

    assert (DataString('A=B\nB')
            .setHardFail(False)
            .upsertEQ('A=B')
            == 'A=B\nB')
    assert (DataString('A=B\nB')
            .setHardFail(False)
            .upsertEQ('A=C')
            == 'A=C\nB')

def test_data_string_upsert_partial():

    # Partials

    assert (DataString('A=b')
            .setHardFail(False)
            .upsert('A=b', 'A=B') == 'A=B')
    assert (DataString('A=b')
            .setHardFail(False)
            .upsert('A=', 'A=B') == 'A=B')
    assert (DataString('A=b')
            .setHardFail(False)
            .upsert(KeyString('A=b'), 'A=B') == 'A=B')

def test_data_string_dups():
    #print('---')
    #print('test',DataString('A\nA', settings={'dup':False, 'hard_fail': False}).replace('\n','|'))
    # attempt dup intialization
    #print('test',DataString('', settings={'dup':False, 'hard_fail': False}).replace('\n','|'))
    # regular

    # dup False
    assert (DataString('',     settings={'dup': False, 'hard_fail': False}) == '')
    assert (DataString('A',    settings={'dup': False, 'hard_fail': False}) == 'A')
    assert (DataString('A\nA', settings={'dup': False, 'hard_fail': False}) == '')

    assert (DataString('A',    settings={'dup': False, 'hard_fail': False}).insert('A') == 'A')
    assert (DataString('A',    settings={'dup': False, 'hard_fail': False}).updateEQ('A=A') == 'A')
    assert (DataString('A=',   settings={'dup': False, 'hard_fail': False}).updateEQ('A=A') == 'A=A')
    assert (DataString('A=A',  settings={'dup': False, 'hard_fail': False}).updateEQ('A=a') == 'A=a')


    # dup True
    assert (DataString('',     settings={'dup': True, 'hard_fail': False}) == '')
    assert (DataString('A',    settings={'dup': True, 'hard_fail': False}) == 'A')
    assert (DataString('A\nA', settings={'dup': True, 'hard_fail': False}) == 'A\nA')
    assert (DataString('A',    settings={'dup': True, 'hard_fail': False}).insert('A') == 'A\nA')
    assert (DataString('A',    settings={'dup': True, 'hard_fail': False}).updateEQ('A=A') == 'A')


def main():


    test_data_string_init()
    test_data_string_delete()
    #test_data_string_insert()

    #test_data_string_updateEQ()

    ##test_data_string_update_partial()
    #test_data_string_upsert()
    #test_data_string_upsert_partial()
    test_data_string_upsertEQ()

    #test_data_string_dups()

if __name__ == "__main__":
    # execute as docker
    main()