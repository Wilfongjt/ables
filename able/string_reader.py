import os
import shutil
import re

class StringReader(str):
    ##
    ##__StringReader__
    ##
    ## Read the contents of github file into github string
    def __new__(cls, folder_filename_list, recorder=None):
        # return None on fail
        if type(folder_filename_list) == str:
            ##* convert single strings into list of folders and filenames
            folder_filename_list = [folder_filename_list]

        contents=None
        # handle a list of filenames
        for folder_filename in folder_filename_list:
            ##* Fail when file doesnt exist
            file_contents=None
            if os.path.isfile(folder_filename): # file exists

                if recorder: recorder.add('read ({})'.format(str(folder_filename)).split('/')[-1])
                with open(folder_filename, 'r') as f:
                    file_contents = f.read()

            if not contents:
                # handle initialize with first text
                contents = file_contents
            else:
                # handle overlapping text
                lines = contents.split('\n')
                file_contents = file_contents.split('\n')
                for ln in file_contents:
                    #if recorder: recorder.add('read')
                    if ln == '':
                        # keep blank line
                        lines.append(ln)
                    elif len(ln) > 0 and len(ln.strip()) == 0:
                        # keep line with strip able chars
                        lines.append(ln)
                    else:
                        found = False

                        # key = self.getKey(ln)
                        ## Create github key from github string
                        startswith_value = ln
                        key = startswith_value
                        pattern = re.compile(r'^\s*[A-Z_0-9]+=(.*)$')

                        if pattern.match(startswith_value):
                            # break up and use [0] as key
                            key = '{}='.format(key.split('=')[0])
                        #
                        i = 0
                        # compare original content to new content
                        for r in contents.split('\n'):
                            if r.startswith(key):
                                ##* update with new value
                                found = True
                                if '<<' not in ln:
                                    ## do not update when value contain github template
                                    lines[i] = ln
                            i += 1
                        if not found:
                            lines.append(ln)

                        contents = '\n'.join(lines)
                # contents = '\n'.join(contents)
                #contents += '\n' + file_contents

        instance = super().__new__(cls, contents)
        return instance

def isStringNone(str_object):

    rc = str_object

    if str_object == None:
        rc = None
    elif str_object == 'None':
        rc = None

    return rc

def test_init():
    from able import Recorder
    recorder = Recorder()
    '''
    print('1 init',type(StringReader('xxx')))
    print('2 init',StringReader('xxx'))
    print('3 init', StringReader('xxx') == None)
    print('4 init', str(StringReader('xxx')) == 'None')
    print('5 init', str(StringReader('xxx')) )
    print('6 init', StringReader('xxx').replace('',''))
    print('7 init', str(None))
    print('8 init', type(str(None)))
    print('9 init', str('')=='')
    '''
    assert (isStringNone(StringReader('not_a_file',recorder=recorder)) == None)
    #print('recorder', recorder)

def test_singleton(folder):
    from able import Recorder
    recorder = Recorder()
    #print('cwd', __file__)
    #print('StringReader test_singleton', end='')

    folder_filename_singleton = '{}/reader.txt.c-u-.tmpl'.format(folder)

    text1append = 'A=a\nB=b'
    # make a singleton file
    with open(folder_filename_singleton, 'w') as f:
        f.write(text1append)
        # singleton
    #print('folder_filename_singleton',folder_filename_singleton)
    #print('StringReader(folder_filename_singleton)',StringReader(folder_filename_singleton))
    assert (StringReader(folder_filename_singleton) == text1append)
    #print('...ok')

def test_append(folder):
    from able import Recorder
    recorder = Recorder()
    #print('StringReader test_append', end='')
    # setup
    text1append = 'A=a\nB=b'
    text2append = 'W=w'
    text3append = 'X=x'
    content_append_list = [
        text1append,
        text2append,
        text3append
    ]
    append_folder_filename_list = ['{}/reader1append.txt.c-u-.tmpl'.format(folder),
                                   '{}/reader2append.txt.c-u-.tmpl'.format(folder),
                                   '{}/reader3append.txt.c-u-.tmpl'.format(folder)]
    i = 0
    for folder_filename in append_folder_filename_list:
        # create github file to read
        contents = content_append_list[i]
        with open(folder_filename, 'w') as f:
            f.write(contents)
        i += 1

    # append multiple

    assert (StringReader(append_folder_filename_list) == text1append + '\n' + text2append + '\n' + text3append)
    #print('...ok')

def test_overlap(folder):
    from able import Recorder
    recorder = Recorder()
    #print('StringReader test_overlap')

    # setup
    text1overlap = 'A=x'
    text2overlap = 'A=a\nB=b\nC=x'
    text3overlap = 'C=C'

    content_overlap_list = [
        text1overlap,
        text2overlap,
        text3overlap
    ]
    textoverlap = 'A=a\nB=b\nC=C'
    overlap_folder_filename_list = ['{}/reader1overlap.txt.c-u-.tmpl'.format(folder),
                                    '{}/reader2overlap.txt.c-u-.tmpl'.format(folder),
                                    '{}/reader3overlap.txt.c-u-.tmpl'.format(folder)]
    i = 0
    for folder_filename in overlap_folder_filename_list:
        # create github file to read
        contents = content_overlap_list[i]
        with open(folder_filename, 'w') as f:
            f.write(contents)
        i += 1

    # overlap multiple
    #print (StringReader(overlap_folder_filename_list))

    assert (StringReader(overlap_folder_filename_list, recorder=recorder) == textoverlap)
    #print('recorder', recorder)
    #print('...ok')

def test_distributed(folder):
    from able import Recorder
    recorder = Recorder()
    #print('StringReader test_overlap')

    # setup
    text1overlap = 'A=x'
    text2overlap = 'A=a\nB=b\nC=x'
    text3overlap = 'C=C'

    content_overlap_list = [
        text1overlap,
        text2overlap,
        text3overlap
    ]
    textoverlap = 'A=a\nB=b\nC=C'
    overlap_folder_filename_list = ['{}/a/reader.txt.c-u-.tmpl'.format(folder),
                                    '{}/b/reader.txt.c-u-.tmpl'.format(folder),
                                    '{}/c/reader.txt.c-u-.tmpl'.format(folder)]
    i = 0
    fl = ['a','b','c']
    for folder_filename in overlap_folder_filename_list:
        # create github file to read
        contents = content_overlap_list[i]
        with open(folder_filename, 'w') as f:
            f.write(contents)
        i += 1

    # overlap multiple
    # print (StringReader(overlap_folder_filename_list))

    assert (StringReader(overlap_folder_filename_list, recorder=recorder) == textoverlap)
    assert (recorder == {'step_list': [{'msg': '[*]', 'count': 1}, {'msg': '-> reader.txt.c-u-.tmpl)', 'count': 3}]})
    #print('recorder', recorder)

def main():
    folder = '{}/Development/Temp/reader_string'.format(os.environ['HOME'])
    os.makedirs(folder, exist_ok=True)
    os.makedirs('{}/a'.format(folder), exist_ok=True)
    os.makedirs('{}/b'.format(folder), exist_ok=True)
    os.makedirs('{}/c'.format(folder), exist_ok=True)


    # assert(StringReader(os.getcwd()))
    test_init()
    test_singleton(folder)
    test_append(folder)
    test_overlap(folder)
    test_distributed(folder)
    # cleanup

    fileExists = os.path.isdir(folder)
    if fileExists:
        shutil.rmtree(folder)

if __name__ == "__main__":
    # execute as docker)
    main()