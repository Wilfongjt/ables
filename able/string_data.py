
# settings {'dup': True}
# Insert means append new-line to the end
# Update means find and replace all found lines
# Upsert means find and replace all found lines otherwise append new-line
# Delete means find and remove all line found lines

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
        instance = super().__new__(cls, contents)
        return instance

    def getSettings(self):
        return self.settings

    def setHardFail(self, tf):
        self.settings['hard_fail']=tf
        return self

    def __append(self, line):
        # append line string without dup check
        # use insert for checking

        if len(self) > 0:
            rc = DataString(self + '\n' + line, self.settings)
        else:
            rc = DataString(line, self.settings)

        return rc
    def matches(self, a, b):
        #if a == '' and a == b:
        #    # handle '' == ''
        #    return False
        if a == '' or b == '':
            return False
        #if a == ''
        return a.startswith(b)

    def find(self, line):
        found = False
        i = 0
        for ln in self.split('\n'):
            #if ln.startswith(line):
            if self.matches(ln, line):
                #print('found {} at {}'.format(line, ln))
                #found = True
                found = {'at': i, 'searching': line}
                break
            i += 1
        return found

    def delete(self, existing_line):
        rc = []
        end = False
        for ln in self.split('\n'):
            # skip the not found lines
            if not self.matches(ln, existing_line):
                rc.append(ln)
        rc = '\n'.join(rc)
        return DataString(rc,self.getSettings())

    def insert(self, new_line):
        rc = None
        if not self.settings['dup']: # no dups
            #print('insert 1', len(self), self.find(new_line))
            # make sure new_line is unique
            found = self.find(new_line) # confirm no dups
            if found:
                #print('insert self ({})'.format(self))
                found['failed']: 'duplicate'
                self.settings['failed']=found
                if self.settings['hard_fail']:
                    raise Exception('Found Duplicate line "{}"'.format(found))
                #print('settings', self.getSettings())
                return self
            rc = self.__append(new_line)
        else:
            #print('insert 2')

            rc = self.__append(new_line)

        return rc

    def update(self, existing_line, new_line):
        i = 0

        if not self.getSettings()['dup'] and existing_line==new_line:
            # avoid this pointless update
            return self

        rc = self.split('\n')
        if not self.getSettings()['dup'] and new_line in rc:
            # stop update when update will cause a duplicate line to be added
            return self

        #print('update', self)

        for ln in rc:

            if self.matches(ln, existing_line):
                #print('matched ({}) and ({})'.format(ln, existing_line))
                if self.getSettings()['dup']:
                    # update all when matched
                    rc[i] = new_line
                    updated = True
                else: # not dup
                    rc[i] = new_line
                    break # only update the first

            i += 1
        rc = '\n'.join(rc)
        return DataString(rc, self.getSettings())

    def upsert(self, existing_line, new_line):
        # print('-- upsert')
        i = 0

        #if not self.getSettings()['dup'] and existing_line==new_line:
        #    # avoid this pointless update
        #    print('1 upsert ', self.replace('\n','|'))
        #    return self

        rc = self.split('\n')

        if not self.getSettings()['dup'] and new_line in rc:
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

            if self.matches(ln, existing_line):
                # print('matched ({}) and ({})'.format(ln, existing_line))
                if self.getSettings()['dup']:
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



def main():
    #print('-', DataString().replace('\n','|'))

    assert (DataString() == '')
    assert(DataString('')=='')
    assert (DataString('A line') == 'A line')
    # insert
    assert(DataString().setHardFail(False).insert('A line')=='A line')
    assert(DataString()
           .setHardFail(False)
           .insert('A line')
           .insert('A line') == 'A line')
    assert(DataString()
           .setHardFail(False)
           .insert('A line')
           .insert('B line') == 'A line\nB line')
    # delete
    assert (DataString().delete('') == '')
    assert (DataString().delete('A line') == '')
    assert (DataString('A line').delete('B line') == 'A line')

    assert (DataString('A line').delete('A line') == '')

    assert(DataString()
           .setHardFail(False)
           .insert('A line')
           .insert('B line')
           .delete('A line') == 'B line')
    assert(DataString()
           .setHardFail(False)
           .insert('A line')
           .insert('B line')
           .delete('B line') == 'A line')

    # update dup=False
    assert (DataString()
            .setHardFail(False)
            .update('', '') == '')
    assert (DataString()
            .setHardFail(False)
            .update('', 'A line')=='')
    assert (DataString('A line')
            .setHardFail(False)
            .update('A line', 'A line')=='A line')

    assert (DataString('A line\nB line')
            .setHardFail(False)
            .update('A line', 'B line')=='A line\nB line')
    assert (DataString('A line\nB line')
            .setHardFail(False)
            .update('A line', 'C line')=='C line\nB line')
    assert (DataString('A line\nB line')
            .setHardFail(False)
            .update('B line', 'C line') == 'A line\nC line')

    # Upsert
    print('--upsert')
    # "" + "" -> ""
    # print('A upsert')
    print("A upsert given '' replace '' with '' -> ''")

    assert (DataString()
            .setHardFail(False)
            .upsert('', '') == '')

    # "" + "A" -> "A"

    print("B upsert given '' replace '' with A  -> A")

    assert (DataString()
            .setHardFail(False)
            .upsert('', 'A')=='A')

    # "A" + "A" -> "A"

    print("C upsert given A  replace A  with A  -> A")

    assert (DataString('A')
            .setHardFail(False)
            .upsert('A', 'A')=='A')

    # "A" + "B -> "A\nB"
    print("D upsert given AB replace A  with B  -> AB")

    assert (DataString('A\nB')
            .setHardFail(False)
            .upsert('A', 'B')=='A\nB')

    #print(DataString('A\nB')
    #        .setHardFail(False)
    #        .upsert('A', 'C'))

    print("E upsert given AB replace A  with C  -> CB")

    assert (DataString('A\nB')
            .setHardFail(False)
            .upsert('A', 'C')=='C\nB')

    #print("'AB'  'C' -> 'ABC'")
    print("F upsert given AB replace B  with C  -> AC")

    assert (DataString('A\nB')
            .setHardFail(False)
            .upsert('B', 'C') == 'A\nC')

    print("G upsert given AB replace '' with C  -> AB")

    assert (DataString('A\nB')
          .setHardFail(False)
          .upsert('', 'C')=='A\nB\nC')

    #exit(0)

    print("H upsert given AB replace C  with C  -> ABC")

    #print (DataString('A\nB')
    #        .setHardFail(False)
    #        .upsert('C', 'C').replace('\n','|'))

    assert (DataString('A\nB')
          .setHardFail(False)
          .upsert('C', 'C') == 'A\nB\nC')


if __name__ == "__main__":
    # execute as docker
    main()