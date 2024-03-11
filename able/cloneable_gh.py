import os
import subprocess
from able import Projectable,Urlable_GH
from able.exceptions.exception_cloning import ExceptionCloning
class Cloneable_GH():
    # (username_gh, repo_folder_gh) ->
    def __init__(self, repo_folder = None, username=None):
        self.failed=False
        self.username=username
        self.repo_folder = repo_folder
        self.GIT_CLONE_TEMPLATE = 'git clone {}'  # project_url

    def clone(self, repo_folder=None, username_gh=None):

        rc = False
        if not repo_folder:
            repo_folder = self.repo_folder # str(self.repo_folder).split('/')[-1]
        if not username_gh:
            username_gh = self.username

        ##* dont overwrite existing clone
        if os.path.isdir(repo_folder):
            return self
        #create workspace folders
        lastdir = os.getcwd()

        os.chdir(Projectable(repo_folder).getBranchFolder())

        project_url=Urlable_GH(username_gh, repo_folder).getUrl_GH()

        command = self.GIT_CLONE_TEMPLATE.format(project_url)
        ret = subprocess.run(command, capture_output=True, shell=True)

        if ret.returncode != 0:
            os.chdir(lastdir)
            raise ExceptionCloning('Cloneable_GH.clone() failed!')
        os.chdir(lastdir)
        return self

def main():
    import shutil
    #from able.test_constants import TestConstants
    organization='test-org'
    project_name = 'py_test'
    workspace='00_clone'
    branch= 'clone_branch'
    username= 'wilfongjt'

    # Create target folder
    ## home/Development/organization/workspace/project/branch/project
    repo_folder = '{}/Development/{}/{}/{}/{}/{}'.format(os.environ['HOME'], organization, workspace, project_name, branch, project_name)
    branch_folder = '{}/Development/{}/{}/{}/{}'.format(os.environ['HOME'], organization, workspace, project_name, branch)

    #print('repo_folder_gh   ', repo_folder)
    #print('branch_folder    ',branch_folder)
    os.makedirs(branch_folder,exist_ok=True)

    assert(Cloneable_GH().clone(repo_folder, username) )
    assert(os.path.isdir(repo_folder))

    # remove target folder and files
    if os.path.isdir(branch_folder):
        shutil.rmtree(repo_folder)

if __name__ == "__main__":
    # execute as docker
    main()