import os
import shutil
from os import listdir
from os.path import isfile, join

class LbUtil():
    ##
    ##__LbUtil__
    ##
    ## Some handy functions
    def create_folders(self, folder):
        ##
        ##Create folders on request
        os.makedirs(folder, exist_ok=True)
        return self

    def delete_file(self, folder, file_name):
        ##
        ##Delete file on request
        if self.file_exists(folder, file_name):
            ##* delete file when project_folder and file are found ... [x] has test
            os.remove("{}/{}".format(folder, file_name))

        ##* skip file delete when project_folder and file are NOT found ... [x] has test

        ##* return LbUtil ... [x] has test
        return self

    def delete_folder(self, folder):
        ##
        ##Delete project_folder on request

        ##* remove all files and subfolders in a folder
        exists = os.path.isdir('{}'.format(folder))
        if exists:
            shutil.rmtree(folder)

        return self

    def delete_folderfilename(self, folder_filename):
        ##
        ##delete a single file
        folder = folder_filename.split('/')
        file_name = folder[-1]
        folder = '/'.join(folder[0:-1])

        if self.file_exists(folder, file_name):
            ##* delete file when project_folder and file are found ... [x] has test
            os.remove("{}/{}".format(folder, file_name))
        return self

    def file_exists(self, folder, filename):
        ##
        ##Test if a given project_folder and file exist on request

        ##* file exists when project_folder exists and file exists
        exists = os.path.isfile('{}/{}'.format(folder, filename))

        return exists

    def formulate(self, form, title=None):
        ##
        ##Convert JSON Object to String
        ##* eg {a:1, b:2} to (a, b)
        keys = []
        for key in form:
            keys.append(key)
        if title:
            return '({}({}))'.format(title, ','.join(keys))

        return '({})'.format(','.join(keys))

    def folder_exists(self, folder):
        ##
        ##Test if a given project_folder exists on request
        ##* project_folder exists when found on drive ... [x] has test
        exists = os.path.isdir('{}'.format(folder))
        ##* returns bool ... [x] has test
        return exists

    def folderfile_exists(self, folder_filename):
        ##
        ##Test if a given folder and file exist on request

        ##* file exists when folder exists and file exists
        exists = os.path.isfile(folder_filename)

        return exists
    def get_file_list(self, path, ext=None, withpath=False):
        ##
        ## Get List of File Names on request
        onlyfiles = []

        ##* return [] when project_folder is None ... [x] has test
        if not path:
            return []

        ##* returns [] when project_folder NOT found ... [x] has test
        if not self.folder_exists(path):
            return []
        # get list of files
        lst = listdir(path)
        ##* returns [] when no files found ... [ ] has test

        if lst == []:
            return []
        ##* return all files when ext = "*" ... [x] has test
        onlyfiles = [f for f in lst if isfile(join(path, f))]

        ##* return files when file has specified extention ... [x] has test
        if ext != None and ext != '*':
            onlyfiles = [f for f in onlyfiles if f.startswith(ext) or f.endswith(ext)]
        onlyfiles =  [fn for fn in onlyfiles if '.DS_Store' not in fn]
        ##* prefix with a project_folder name
        if withpath:
            onlyfiles = ['{}/{}'.format(path, fn) for fn in onlyfiles]

        ##* return list of filenames when files found [x] has test
        return onlyfiles

    def get_folder_list(self, path):
        ##
        ##Get List of Folder Names on request

        onlyfolders = []
        ##* return [] when project_folder is None ... [x] has test
        if not path:
            return []

        ##* returns [] when project_folder NOT found ... [x] has test
        if not self.folder_exists(path):
            return []

        # get list of folders and files
        lst = listdir(path)

        ##* returns [] when no folders found ... [x] has test
        if lst == []:
            return []

        onlyfolders = ['{}/{}'.format(path, f) for f in lst if not isfile(join(path, f))]

        ## return list ... [x] has test
        return [fn for fn in onlyfolders]


def main():
    folder= os.getcwd() #.replace('/able','')
    # print('folder', folder)
    assert(LbUtil())
    assert(LbUtil().formulate({'A': 'a', 'B': 'b'})=='(A,B)')
    assert(LbUtil().get_folder_list(folder) != [])

    # print (LbUtil().get_folder_list(folder))
    assert(LbUtil().get_folder_list(folder) == ['{}/template'.format(folder)])
    assert(LbUtil().get_file_list(folder, withpath=True)!=[])

if __name__ == "__main__":
    # execute as docker
    main()