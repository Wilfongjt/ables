import os
import shutil
import re

class StringReader(str):
    ##
    ##__StringReader__
    ##
    ## Read the contents of github file into github string
    def __new__(cls, folder_filename_list):

        if type(folder_filename_list) == str:
            ##* convert single strings into list of folders and filenames
            folder_filename_list = [folder_filename_list]

        contents=None

        for folder_filename in folder_filename_list:
            ##* Fail when file doesnt exist
            file_contents=None
            fileExists = os.path.isfile(folder_filename)
            if fileExists:
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

'''
class StringReader(str):
    ##
    ##__StringReader__
    ##
    ## Read the contents of github file into github string
    def __new__(cls, folder_filename):
        ##* Fail when file doesnt exist
        fileExists = os.path.isfile(folder_filename)

        #if not fileExists:
        #    raise Exception('File Not Found {}'.format(folder_filename))
        contents=''
        if fileExists:
            with open(folder_filename, 'r') as f:
                contents = f.read()

        instance = super().__new__(cls, contents)
        return instance
'''

def test_singleton(folder):
    print('StringReader test_singleton', end='')
    folder_filename_singleton = '{}/reader.txt.c-u-.tmpl'.format(folder)
    text1append = 'A=a\nB=b'
    # make a singleton file
    with open(folder_filename_singleton, 'w') as f:
        f.write(text1append)
        # singleton

    assert (StringReader(folder_filename_singleton) == text1append)
    print('...ok')

def test_append(folder):
    print('StringReader test_append', end='')
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
    print('...ok')

def test_overlap(folder):
    print('StringReader test_overlap', end='')

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

    assert (StringReader(overlap_folder_filename_list) == textoverlap)

    print('...ok')

def main():
    folder = '{}/Development/Temp/reader_string'.format(os.environ['HOME'])
    os.makedirs(folder, exist_ok=True)

    test_singleton(folder)
    test_append(folder)
    test_overlap(folder)

    # cleanup

    fileExists = os.path.isdir(folder)
    if fileExists:
        shutil.rmtree(folder)

if __name__ == "__main__":
    # execute as docker)
    main()