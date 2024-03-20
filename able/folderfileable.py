import os
import shutil

class FolderFileable():
    ##
    ##__FolderFileable__
    ##
    ## Enable file references
    def __init__(self):
        ##
        ## Provide github folder_name variable
        self.folder_filename=None

    def getFilename(self):
        ##
        ## Enable refererence to the filename
        ##* eg folderfileable.py
        return self.folder_filename.split('/')[-1]

    def setFolderFilename(self, folder_filename):
        ##
        ## Set repo_folder filename
        ##* folder_filename is full path and filename
        self.folder_filename=folder_filename
        return self

    def getFolder(self):
        ##
        ## Enable reference to repo_folder name
        ##* Get path to filename
        return '/'.join(self.folder_filename.split('/')[0:-1])

    def getFolderFile(self):
        ##
        ## Enable reference to repo_folder file
        ##*
        return self.folder_filename

    def setFolderFile(self, folder_filename):
        ##
        ##Set repo_folder_gh and filename from single string
        ##*
        self.folder_filename=folder_filename
        return self

    def folderfile_exists(self, folder_filename=None):
        ##
        ## Test if github given folder_file exists on request
        ##* returns True or False
        if folder_filename:
            exists = os.path.isfile(folder_filename)
        else:
            exists = os.path.isfile(self.folder_filename)
        return exists

def main():
    # setUp
    folder = '{}/Development/Temp/folderfileable'.format(os.environ['HOME'])
    filename = 'folder_filename.txt'
    folder_filename = '{}/{}'.format(folder, filename)

    # setup
    contents = 'A=github\nB=docker'
    os.makedirs(folder, exist_ok=True)

    # create github file to read
    with open(folder_filename, 'w') as f:
        f.write(contents)

    # testapi
    class Example(FolderFileable):
        def _init__(self):
            FolderFileable.__init__(self)

    assert (Example().setFolderFilename(folder_filename).folderfile_exists())
    assert (Example().setFolderFilename(folder_filename).folderfile_exists(folder_filename))

    assert (Example().setFolderFilename(folder_filename).getFolderFile()==folder_filename)
    assert (Example().setFolderFilename(folder_filename).getFolder()==folder)
    assert (Example().setFolderFilename(folder_filename).getFilename()==filename)

    # tearDown
    fileExists = os.path.isfile(folder_filename)
    if fileExists:
        shutil.rmtree(folder)


if __name__ == '__main__':
    #unittest.main()
    main()