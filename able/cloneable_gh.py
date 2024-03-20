import os
import subprocess

from able.exception_cloning import ExceptionCloning
class Cloneable_GH():
    # (username_gh, repo_folder_gh) ->
    def __init__(self, repo_folder = None, username=None):
        self.failed=False
        self.username=username
        self.repo_folder = repo_folder
        self.GIT_CLONE_TEMPLATE = 'git clone {}'  # project_url
        self.GIT_URL_TEMPLATE = 'https://github.com/{}/{}.git'

    def clone(self, repo_folder=None, username_gh=None):

        rc = False
        if not repo_folder:
            repo_folder = self.repo_folder # str(self.repo_folder).split('/')[-1]
        if not username_gh:
            username_gh = self.username

        ##* dont overwrite existing clone
        if os.path.isdir(repo_folder):
            return self
        # create workspace folders
        lastdir = os.getcwd()

        branch_folder = '/'.join(repo_folder.split('/')[0:-1])
        # print('repo_folder', repo_folder)
        # print('repo branch_folder', branch_folder)
        os.chdir(branch_folder)
        # os.chdir(Projectable(repo_folder).getBranchFolder())

        # project_url=Urlable_GH(username_gh, repo_folder).getUrl_GH()
        project_url=self.GIT_URL_TEMPLATE.format(username_gh, repo_folder.split('/')[-1])
        command = self.GIT_CLONE_TEMPLATE.format(project_url)
        ret = subprocess.run(command, capture_output=True, shell=True)
        # print('Cloneable_GH clone ret', ret)
        if ret.returncode != 0:
            os.chdir(lastdir)
            raise ExceptionCloning('Cloneable_GH.clone() failed!')
        os.chdir(lastdir)
        return self


def main():
    import shutil
    #from able.test_constants import TestConstants
    organization='testapi-org'
    project_name = 'py_test'
    workspace='00_clone'
    branch= 'clone_branch_test'
    username= 'wilfongjt'

    # Create target repo_folder
    ## home/Development/organization/workspace/project/branch/project
    repo_folder = '{}/Development/{}/{}/{}/{}/{}'.format(os.environ['HOME'],
                                                         organization,
                                                         workspace,
                                                         project_name,
                                                         branch,
                                                         project_name)
    project_folder = '{}/Development/{}/{}/{}'.format(os.environ['HOME'],
                                                           organization,
                                                           workspace,
                                                           project_name)
    branch_folder = '{}/Development/{}/{}/{}/{}'.format(os.environ['HOME'],
                                                        organization,
                                                        workspace,
                                                        project_name,
                                                        branch)

    #print('repo_folder_gh   ', repo_folder)
    #print('branch_folder    ',branch_folder)
    os.makedirs(branch_folder,exist_ok=True)

    # Test
    assert(Cloneable_GH().clone(repo_folder, username))
    assert(os.path.isdir(repo_folder))

    # remove target repo_folder and files
    if os.path.isdir(branch_folder):
        shutil.rmtree(project_folder)

if __name__ == "__main__":
    # execute as docker
    main()