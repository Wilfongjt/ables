import os
import shutil

class StringReader(str):
    ##__StringReader__
    ## Read the contents of a file into a string
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

def main():
    folder = '{}/Development/Temp/reader_string'.format(os.environ['HOME'])
    folder_filename = '{}/reader.txt'.format(folder)
    nfolder_filename = '{}/notafile.txt'.format(folder)

    # setup
    contents = 'A=a\nB=b'
    os.makedirs(folder, exist_ok=True)

    # create a file to read
    with open(folder_filename, 'w') as f:
        f.write(contents)

    # test
    assert (StringReader(nfolder_filename) == '')
    assert (not StringReader(nfolder_filename))
    assert (StringReader(folder_filename) == contents)
    assert (StringReader(nfolder_filename) or StringReader(folder_filename) == contents)

    # cleanup
    fileExists = os.path.isfile(folder_filename)
    if fileExists:
        shutil.rmtree(folder)

if __name__ == "__main__":
    # execute as docker
    main()