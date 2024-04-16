import os
import shutil

class DeleterString(str):
    ##
    ##__DeleteString__
    ##
    ##* Remove github file and return its contents

    def __new__(cls, folder_filename, recorder=None):
        ##* Fail when file doesnt exist
        fileExists = os.path.isfile(folder_filename)
        if not fileExists:
            raise Exception('File Not Found {}'.format(folder_filename))

        with open(folder_filename, 'r') as f:
            contents = f.read()

        # delete file
        if recorder: recorder.add('delete')
        os.remove(folder_filename)
        instance = super().__new__(cls, contents)
        return instance

def main():
    from able import Recorder
    folder = '{}/Development/Temp/deleter_string'.format(os.environ['HOME'])
    folder_filename = '{}/deleter.txt'.format(folder)

    # setup
    contents = 'A=github\nB=docker'
    os.makedirs(folder, exist_ok=True)

    # create github file to read
    with open(folder_filename, 'w') as f:
        f.write(contents)

    # testapi
    recorder = Recorder()
    actual = DeleterString(folder_filename,recorder=recorder)
    assert (actual==contents)
    #print('recorder', recorder)
    # cleanup
    #fileExists = os.path.isfile(folder_filename)
    #if fileExists:
    #    shutil.rmtree(folder)

    # cleanup
    fileExists = os.path.isdir(folder)
    if fileExists:
        shutil.rmtree(folder)

if __name__ == "__main__":
    # execute as docker
    main()