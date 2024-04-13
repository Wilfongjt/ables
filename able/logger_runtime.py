import os

from able.folderfileable import FolderFileable

class RuntimeLogger(str):
    ##
    ##__RuntimeLogger__
    ##
    ## Write a string to the runtime.log file
    def __new__(cls, project_name='runtime'):

        di = os.getcwd().split('/').index('Development') + 4 # project nane

        project_folder = os.getcwd().split('/')[0:di]
        #project_name = project_folder[-1]
        project_folder.append('log')
        project_folder = '/'.join(project_folder)
        os.makedirs(project_folder, exist_ok=True)

        contents = '{}/{}.log'.format(project_folder, project_name)
        print('contents', contents)
        instance = super().__new__(cls, contents)
        return instance

    def write(self, content_string):
        with open(self, 'a') as f:
            self.last_line=content_string
            f.write('{}\n'.format(content_string))
        return self

def main():
    import shutil
    # make a temp folder

    actual = RuntimeLogger()
    assert(actual)
    actual.write('hi').write('hi')

    # cleanup
    #if os.path.isfile(log_folderfile):
    #    shutil.rmtree(temp_folder)

if __name__ == "__main__":
    # execute as docker
    main()