import os
import shutil

class LbUtil():

    def create_folders(self, folder):
        ##* create folders on request
        os.makedirs(folder, exist_ok=True)
        return self

    def delete_file(self, folder, file_name):
        ##* Delete file on request
        if self.file_exists(folder, file_name):
            ##* delete file when project_folder and file are found ... [x] has test
            os.remove("{}/{}".format(folder, file_name))

        ##* skip file delete when project_folder and file are NOT found ... [x] has test

        ##* return LbUtil ... [x] has test
        return self

    def delete_folder(self, folder):
        ##* Delete project_folder on request

        ##* remove all files and subfolders in a folder
        exists = os.path.isdir('{}'.format(folder))
        if exists:
            shutil.rmtree(folder)

        return self

    def delete_folderfilename(self, folder_filename):
        ##__delete_folderfilename__
        ##* delete a single file
        folder = folder_filename.split('/')
        file_name = folder[-1]
        folder = '/'.join(folder[0:-1])

        if self.file_exists(folder, file_name):
            ##* delete file when project_folder and file are found ... [x] has test
            os.remove("{}/{}".format(folder, file_name))
        return self

    def file_exists(self, folder, filename):
        ##* Test if a given project_folder and file exist on request

        ##* file exists when project_folder exists and file exists
        exists = os.path.isfile('{}/{}'.format(folder, filename))

        return exists

    def folder_exists(self, folder):
        ##* Test if a given project_folder exists on request
        ##* project_folder exists when found on drive ... [x] has test
        exists = os.path.isdir('{}'.format(folder))
        ##* returns bool ... [x] has test
        return exists

    def folderfile_exists(self, folder_filename):
        ##* Test if a given folder and file exist on request

        ##* file exists when folder exists and file exists
        exists = os.path.isfile(folder_filename)

        return exists


def main():
    assert(LbUtil())

if __name__ == "__main__":
    # execute as docker
    main()