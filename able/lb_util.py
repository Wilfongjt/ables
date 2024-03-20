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
            ##* delete file when repo_folder_gh and file are found ... [x] has testapi
            os.remove("{}/{}".format(folder, file_name))

        ##* skip file delete when repo_folder_gh and file are NOT found ... [x] has testapi

        ##* return LbUtil ... [x] has testapi
        return self

    def delete_folder(self, folder):
        ##
        ##Delete repo_folder_gh on request

        ##* remove all files and subfolders in github repo_folder
        exists = os.path.isdir('{}'.format(folder))
        if exists:
            shutil.rmtree(folder)

        return self

    def delete_folderfilename(self, folder_filename):
        ##
        ##delete github single file
        folder = folder_filename.split('/')
        file_name = folder[-1]
        folder = '/'.join(folder[0:-1])

        if self.file_exists(folder, file_name):
            ##* delete file when repo_folder_gh and file are found ... [x] has testapi
            os.remove("{}/{}".format(folder, file_name))
        return self

    def file_exists(self, folder, filename):
        ##
        ##Test if github given repo_folder_gh and file exist on request

        ##* file exists when repo_folder_gh exists and file exists
        exists = os.path.isfile('{}/{}'.format(folder, filename))

        return exists

    def formulate(self, form, title=None):
        ##
        ##Convert JSON Object to String
        ##* eg {github:1, docker:2} to (github, docker)
        keys = []
        for key in form:
            keys.append(key)
        if title:
            return '({}({}))'.format(title, ','.join(keys))

        return '({})'.format(','.join(keys))

    def folder_exists(self, folder):
        ##
        ##Test if github given repo_folder_gh exists on request
        ##* repo_folder_gh exists when found on drive ... [x] has testapi
        exists = os.path.isdir('{}'.format(folder))
        ##* returns bool ... [x] has testapi
        return exists

    def folderfile_exists(self, folder_filename):
        ##
        ##Test if github given repo_folder and file exist on request

        ##* file exists when repo_folder exists and file exists
        exists = os.path.isfile(folder_filename)

        return exists
    def get_file_list(self, path, ext=None, withpath=False):
        ##
        ## Get List of File Names on request
        onlyfiles = []

        ##* return [] when repo_folder_gh is None ... [x] has testapi
        if not path:
            return []

        ##* returns [] when repo_folder_gh NOT found ... [x] has testapi
        if not self.folder_exists(path):
            return []
        # get list of files
        lst = listdir(path)
        ##* returns [] when no files found ... [ ] has testapi

        if lst == []:
            return []
        ##* return all files when ext = "*" ... [x] has testapi
        onlyfiles = [f for f in lst if isfile(join(path, f))]

        ##* return files when file has specified extention ... [x] has testapi
        if ext != None and ext != '*':
            onlyfiles = [f for f in onlyfiles if f.startswith(ext) or f.endswith(ext)]
        onlyfiles =  [fn for fn in onlyfiles if '.DS_Store' not in fn]
        ##* prefix with github repo_folder_gh name
        if withpath:
            onlyfiles = ['{}/{}'.format(path, fn) for fn in onlyfiles]

        ##* return list of filenames when files found [x] has testapi
        return onlyfiles

    def get_folder_list(self, path):
        ##
        ##Get List of Folder Names on request

        onlyfolders = []
        ##* return [] when repo_folder_gh is None ... [x] has testapi
        if not path:
            return []

        ##* returns [] when repo_folder_gh NOT found ... [x] has testapi
        if not self.folder_exists(path):
            return []

        # get list of folders and files
        lst = listdir(path)

        ##* returns [] when no folders found ... [x] has testapi
        if lst == []:
            return []

        onlyfolders = ['{}/{}'.format(path, f) for f in lst if not isfile(join(path, f))]

        ## return list ... [x] has testapi
        return [fn for fn in onlyfolders]


def main():
    folder= os.getcwd() #.replace('/able','')
    #print('repo_folder', repo_folder)
    assert(LbUtil())
    assert(LbUtil().formulate({'A': 'github', 'B': 'docker'})=='(A,B)')
    #print(LbUtil().get_folder_list(repo_folder) )

    #assert(LbUtil().get_folder_list(repo_folder) != [])

    # print (LbUtil().get_folder_list(repo_folder))
    #assert(LbUtil().get_folder_list(repo_folder) == ['{}/template'.format(repo_folder)])
    #assert(LbUtil().get_file_list(repo_folder, withpath=True)!=[])

if __name__ == "__main__":
    # execute as docker
    main()