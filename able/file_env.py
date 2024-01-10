import datetime
import os.path
import shutil
import re
from able.folderfileable import FolderFileable
from able.string_reader import ReaderString

class FileEnv(list, FolderFileable):
    ##* create with defaults when file doesnt exist
    ##* read when file exists
    ##* by default, expect .env in the folder where script is running
    def __init__(self, folder_filename=None):
        FolderFileable.__init__(self)
        # load from current folder
        # fail if .env not found
        #self.setFolderFilename(folder_filename)
        if folder_filename:
            self.setFolderFilename(folder_filename)
        elif os.getcwd().endswith('able'):
            ffn = '{}/.env'.format(os.getcwd())
            # In testing folder
            ##* by default, put .env file in parent folder
            parent_folder = '/'.join(os.getcwd().split('/')[0:-1])
            parent_folderfile = '{}/.env'.format(parent_folder)
            ffn = parent_folderfile
            self.setFolderFilename(ffn)


    def create(self, default_contents):
        raise Exception('.env must be manually created.')
        return self

    def read(self):
        # if file exists, read it, load vars into memory
        if not os.path.isfile(self.getFolderFile()):
            raise Exception('.env must be manually created.')
        contents = ReaderString(self.getFolderFile())
        for ln in contents.split('\n'):

            # Define the regular expression pattern
            pattern = r'^([A-Z][A-Z0-9_]+)=(.+)'

            # Use re.match() to match the entire input string
            match = re.match(pattern, ln)
            if match:
                self.append(ln)
                ln = ln.split('=')
                os.environ[ln[0]]=ln[1]
            else:
                self.append(ln)
        return self
    def update(self):
        raise Exception('.env must be manually updated.')
        return self
    def delete(self):
        raise Exception('.env must be manually deleted.')
        return self

'''    
class Envable():
    ##
    ##__Envable__
    ##
    ## Load env variables from a file
    def __init__(self, envfolderfile=None):
        self.envfolderfile=envfolderfile
        self.create_env(envfolderfile)

    def create_env(self, envfolderfile=None):
        if not envfolderfile:
            envfolderfile=self.envfolderfile
        ##* create
        exists = os.path.isfile(envfolderfile)
        #if not LbUtil().folderfile_exists(envfolderfile):
        if exists:    
            ##* create empty .env file when file is not found
            with open(envfolderfile, 'w') as f:
                f.write('# Created {}'.format(datetime.datetime.now()))
        return self

    def read_env(self, envfolderfile=None):
        ##* Load env variable from a file on request
        if not envfolderfile:
            envfolderfile = self.envfolderfile

        ##* read file new_contents given a folder and filename
        with open(envfolderfile) as f:
            default_contents = f.read()

            # Define the regular expression pattern
            pattern = r'^([A-Z][A-Z0-9_]+)=(.+)'
            for ln in default_contents.split('\n'):
                ##* Process search_line when search_line matches '^([A-Z][A-Z0-9_]+)=(.+)'
                # Use re.match() to match the entire input string
                match = re.match(pattern, ln)
                if match:
                    ln = ln.split('=')
                    #print('match', ln)
                    os.environ[ln[0]]=ln[1]

        return self

    def update_env(self, envfolderfile=None):
        ##* Save env file based on current env variables and env file new_contents on request
        if not envfolderfile:
            envfolderfile = self.envfolderfile
        output_list = []
        ##* read file new_contents given a folder and filename
        with open(envfolderfile) as f:
            default_contents = f.read()
            # Define the regular expression pattern
            pattern = r'^([A-Z][A-Z0-9_]+)=(.+)'
            for ln in default_contents.split('\n'):
                ##* Process search_line when search_line matches '^([A-Z][A-Z0-9_]+)=(.+)'
                # Use re.match() to match the entire input string
                match = re.match(pattern, ln)
                if match:
                    ln = ln.split('=')
                    #print('match', ln)
                    ln = '{}={}'.format(ln[0], os.environ[ln[0]])

                output_list.append(ln)
            output_list = '\n'.join(output_list)

            #print('new env')
            #print(output_list)
            #print('envfolderfile', envfolderfile)
            Saveable(envfolderfile).save(contents=output_list)

        return self
'''
def main():
    # setUp
    folder = '{}/Development/client/workspace/project'.format(os.environ['HOME'])
    filename = 'sample.env'
    folder_filename = '{}/{}'.format(folder,filename)
    os.makedirs(folder, exist_ok=True)
    contents = 'A=a\nB=b'
    contents = '# enviroment variables\n'
    contents += '# format example, delete next line when not needed\n'
    contents += 'SAMPLE_VALUE=abc'

    with open(folder_filename, 'w') as f:
        print('create test file', folder_filename)
        f.write(contents)
    # test

    #assert (CreatorString(folder_filename, contents, overwrite=True) == contents)
    #assert (CreatorString(folder_filename, contents, overwrite=True) == contents)

    assert(FileEnv(folder_filename).getFolderFile()==folder_filename)
    assert(FileEnv(folder_filename).read()==contents.split('\n'))
    assert('SAMPLE_VALUE' in os.environ)
    assert('abc' ==  os.environ['SAMPLE_VALUE'])

    #print('FileEnv 1',FileEnv(folder_filename).getFolderFile())
    #assert(FileEnv().setFolderFilename(folder_filename).getFolderFile()==folder_filename)

    #print(FileEnv().setFolderFilename(folder_filename).create_env(contents))

    #assert(FileEnv().setFolderFilename(folder_filename).create_env(contents)==contents.split('\n'))


    # tearDown

    # cleanup
    if os.path.isfile(folder_filename):
        shutil.rmtree(folder)

if __name__ == '__main__':
    #unittest.main()
    main()