import os
import shutil

class UpdaterString(str):
    ##__FileReadable__
    ##* enable standalone version for testing and ad hoc cases

    def __new__(cls, folder_filename, search_line, new_content):
        ##* Fail when file doesnt exist
        fileExists = os.path.isfile(folder_filename)
        if not fileExists:
            raise Exception('File Not Found {}'.format(folder_filename))
        # get existing content
        with open(folder_filename, 'r') as f:
            contents = f.read()
        # find and replace search_line with new_content
        temp_content=[]
        found=False
        for ln in contents.split('\n'):
            if ln.startswith(search_line):
                found=True
                temp_content.append(new_content)
            else:
                temp_content.append(ln)
        if not found:
            # insert at end
            temp_content.append(new_content)

        contents = '\n'.join(temp_content)
        # save
        with open(folder_filename, 'w') as f:
            f.write(contents)

        instance = super().__new__(cls, contents)
        return instance

def main():
    from able import ReaderString
    folder = '{}/Development/Temp/updater_string'.format(os.environ['HOME'])
    folder_filename = '{}/updater.txt'.format(folder)

    # setup
    contents = 'A=a\nB=b'
    os.makedirs(folder, exist_ok=True)

    # create a file to read
    with open(folder_filename, 'w') as f:
        f.write(contents)

    # test

    assert (UpdaterString(folder_filename,'A=','A=A')=='A=A\nB=b')
    assert (ReaderString(folder_filename)=='A=A\nB=b')
    assert (UpdaterString(folder_filename,'B=','B=B')=='A=A\nB=B')
    assert (ReaderString(folder_filename)=='A=A\nB=B')
    assert (UpdaterString(folder_filename,'C=','C=C')=='A=A\nB=B\nC=C')
    assert (ReaderString(folder_filename)=='A=A\nB=B\nC=C')

    # cleanup
    fileExists = os.path.isfile(folder_filename)
    if fileExists:
        shutil.rmtree(folder)

if __name__ == "__main__":
    # execute as docker
    main()