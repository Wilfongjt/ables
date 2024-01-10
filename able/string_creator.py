import os
import shutil


class CreatorString(str):
    ##__FileReadable__
    ##* enable standalone version for testing and ad hoc cases
    def __init__(self, folder_filename, default_contents, overwrite=False):
        ##* default_contents eg 'A' or 'A=a\nB=b'

        self.folder_filename=folder_filename

    def __new__(cls, folder_filename, default_contents, overwrite=False):
        ##* Fail when file exists and overwrite is False
        fileExists = os.path.isfile(folder_filename)

        if fileExists:
            # file exists
            if overwrite:
                # overwrite is true
                with open(folder_filename, 'w') as f:
                    f.write(default_contents)
            else:
                # overwrite is false
                raise Exception('Create file failed, file exists and no overwrite: {}'.format(folder_filename))
        else:
            # file doesnt exist
            with open(folder_filename, 'w') as f:
                f.write(default_contents)
        instance = super().__new__(cls, default_contents)
        return instance

def main():
    from able.lb_util import LbUtil
    #from file_createable import FileCreateable
    folder = '{}/Development/Temp/create_string'.format(os.environ['HOME'])
    folder_file = '{}/create_string.txt'.format(folder)

    # setup
    contents = 'A=a\nB=b'
    os.makedirs(folder, exist_ok=True)

    # test
    assert (CreatorString(folder_file, contents, overwrite=True) == contents)
    assert (os.path.isfile(folder_file))
    #assert (CreatorString(folder_file, contents, overwrite=True) == contents)


    #try:
    #    assert (CreatorString(folder_file, contents) == contents)
    #    assert (os.path.isfile(folder_file))
    #except as ex:
    #    print('running clean up', ex)

    # cleanup
    if os.path.isfile(folder_file):
        shutil.rmtree(folder)


if __name__ == "__main__":
    # execute as docker
    main()