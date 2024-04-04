import os
import shutil

class Projectable():
    ##
    ##__Projectable__
    ##
    ##* lb_project repo_folder eg Development/client/workspace/lb_project
    ##* branch repo_folder  eg Development/client/workspace/lb_project/branch
    ##* repo repo_folder    eg Development/client/workspace/lb_project/branch/repo

    def __init__(self, repo_folder=None):
        self.repo_folder=repo_folder

    def setRepoFolder(self, repo_folder):
        ##* set repo repo_folder on request eg Development/client/workspace/lb_project/branch/repo
        self.repo_folder = repo_folder
        return self

    def getRepoName(self):
        ##* retrive the GitHub repo name from the repo_folder_gh
        if not self.repo_folder:
            return None
        return self.repo_folder.split('/')[-1]

    def getBranchName(self):
        ##* retrive the GitHub branch name from the repo_folder_gh
        if not self.repo_folder:
            return None
        return self.repo_folder.split('/')[-2]

    def getProjectName(self):
        ##* retrive the GitHub lb_project name from the repo_folder_gh
        if not self.repo_folder:
            return None
        return self.repo_folder.split('/')[-3]

    def getWorkspaceName(self):
        ##* retrive the GitHub workspace name from the repo_folder_gh
        if not self.repo_folder:
            return None
        return self.repo_folder.split('/')[-4]

    def getClientName(self):
        ##* retrive the GitHub client name from the repo_folder_gh
        if not self.repo_folder:
            return None
        return self.repo_folder.split('/')[-5]

    def getDevelopmentFolder(self):
        ##* Enable reference to the development repo_folder

        if not self.repo_folder:
            return None
        ws = '/'.join(self.repo_folder.split('/')[0:-5])
        return ws

    def getClientFolder(self):
        ##* Enable reference to the client repo_folder

        if not self.repo_folder:
            return None
        ws = '/'.join(self.repo_folder.split('/')[0:-4])
        return ws

    def getWorkspaceFolder(self):
        ##* Enable reference to the workspace repo_folder
        if not self.repo_folder:
            return None
        return '/'.join(self.repo_folder.split('/')[0:-3])

    def getProjectFolder(self):
        ##* Enable reference to the lb_project repo_folder
        if not self.repo_folder:
            return None
        return '/'.join(self.repo_folder.split('/')[0:-2])

    def getBranchFolder(self):
        ##* Enable reference to the lb_project repo_folder
        if not self.repo_folder:
            return None
        return '/'.join(self.repo_folder.split('/')[0:-1])

    def getRepoFolder(self):
        ##* Enable setting github reference to repo repo_folder

        if not self.repo_folder:
            return None
        ws = '/'.join(self.repo_folder.split('/'))
        return ws

def main():
    # setup
    folder = '{}/Development/client/workspace/lb_project/branch/repo'.format(os.environ['HOME'])
    expected = '{}/Development/client'.format(os.environ['HOME'])
    repo_folder_name = 'repo'
    os.makedirs(folder, exist_ok=True)

    # testapi
    class Example(Projectable):
        def __init__(self):
            Projectable.__init__(self)

    assert (Example().setRepoFolder(folder).getClientFolder() == '{}/Development/client'.format(os.environ['HOME']))
    assert (Example().setRepoFolder(folder).getWorkspaceFolder() == '{}/Development/client/workspace'.format(os.environ['HOME']))
    assert (Example().setRepoFolder(folder).getDevelopmentFolder() == '{}/Development'.format(os.environ['HOME']))
    assert (Example().setRepoFolder(folder).getProjectFolder() == '{}/Development/client/workspace/lb_project'.format(os.environ['HOME']))
    assert (Example().setRepoFolder(folder).getBranchFolder() == '{}/Development/client/workspace/lb_project/branch'.format(os.environ['HOME']))
    assert (Example().setRepoFolder(folder).getRepoFolder() == '{}/Development/client/workspace/lb_project/branch/repo'.format(os.environ['HOME']))

    assert (Example().setRepoFolder(folder).getClientName() == 'client')
    assert (Example().setRepoFolder(folder).getWorkspaceName() == 'workspace')
    assert (Example().setRepoFolder(folder).getProjectName() == 'lb_project')
    assert (Example().setRepoFolder(folder).getBranchName() == 'branch')
    assert (Example().setRepoFolder(folder).getRepoName() == 'repo')

    # tearDown
    if os.path.isdir('{}'.format(folder)):
        shutil.rmtree(folder)


if __name__ == "__main__":
    # execute as docker
    main()