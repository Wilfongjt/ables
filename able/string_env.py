from able.string_reader import StringReader
import os
import shutil
import re

class EnvString(str):
    ##
    ##__EnvString__
    ##
    ## Environment Variables and Values
    def __new__(cls, env_var_string):

        contents = env_var_string
        for ln in contents.split('\n'):

            # Define the regular expression pattern  r'^([A-Z][A-Z0-9_]+)=(.+)'
            pattern = r'^([A-Z][A-Z0-9_]+)=(.+)'

            # Use re.match() to match the entire input string
            match = re.match(pattern, ln)
            if match:
                ln = ln.split('=')
                ##* loads env variables into memory
                os.environ[ln[0]] = ln[1]

        instance = super().__new__(cls, contents)
        return instance

def main():

    folder = '{}/Development/Temp/env_string'.format(os.environ['HOME'])
    folder_filename = '{}/env_string.env'.format(folder)

    # setup
    contents = 'AAAAA=a\nBBBBB=b'
    os.makedirs(folder, exist_ok=True)

    # create a file to read
    with open(folder_filename, 'w') as f:
        f.write(contents)

    # test
    assert (EnvString(StringReader(folder_filename))==contents)
    assert (os.environ['AAAAA']=='a')
    assert (os.environ['BBBBB']=='b')
    print('EnvString', EnvString(StringReader(folder_filename)))


    # cleanup
    fileExists = os.path.isfile(folder_filename)
    if fileExists:
        shutil.rmtree(folder)

if __name__ == "__main__":
    # execute as docker
    main()