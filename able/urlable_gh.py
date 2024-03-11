import os

from able import Projectable

class Urlable_GH():
    ##
    ##
    # (username_gh, repo_folder_gh) ->
    #def __init__(self):
    #    # repo_folder_gh is for testing
    #    self.GIT_URL_TEMPLATE = 'https://github.com/{}/{}.git'

    def __init__(self, username_gh=None, repo_folder_gh=None):
        # repo_folder_gh is for testing
        self.repo_name_gh = repo_folder_gh
        self.username_gh=username_gh
        self.GIT_URL_TEMPLATE = 'https://github.com/{}/{}.git'

    #def getUrl_GH(self, username_gh=None, project_name_gh=None):
    #    ##
    #    return self.GIT_URL_TEMPLATE.format(username_gh, project_name_gh)


    def getUrl_GH(self, username_gh=None, repo_folder_gh=None):
        if not username_gh:
            username_gh = self.username_gh
        if not repo_folder_gh:
            repo_folder_gh = self.repo_name_gh

        project_url = self.GIT_URL_TEMPLATE.format(username_gh, repo_folder_gh.split('/')[-1])

        return project_url

def main():
    organization = 'test-org'
    workspace='00_clone'
    branch_name='urlable_gh'
    project_name='py_test'
    repo_name='py_test'
    user_name = 'wilfongjt'
    repo_folder = '{}/Developement/{}/{}/{}/{}/{}'.format(os.environ['HOME'],
                                                    organization,
                                                    workspace,
                                                    project_name,
                                                    branch_name,
                                                    repo_name)

    project_name = 'py_test'
    #print('Urlable_GH', Urlable_GH().getUrl_GH(username,project_name))
    assert(Urlable_GH().getUrl_GH(user_name,repo_folder) == 'https://github.com/wilfongjt/py_test.git')

if __name__ == "__main__":
    # execute as docker
    main()