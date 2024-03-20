
class Userable_GH():
    ##
    ##__Userable_GH__
    ##
    ## Provide the abilty to format github Github user naem
    ##
    def __init__(self,username_gh=None):
        # username_gh is for testing
        self.username_gh = username_gh

    def getUsername_GH(self):
        return self.username_gh
    def setUsername_GH(self, username):
        self.username_gh=username
        return self


def main():
    import os
    #twidth = 25
    project_name = 'py_test'  # 'abilities' #'harvest' # 'py_test'
    organization = 'testapi-org'  # 'lyttlebit' # 'temp-org'
    workspace = 'ws-testapi'  # 'ws_abilities'
    username_gh = 'wilfongjt'
    #repo_folder_gh = '{}/Development/{}/{}/{}'.format(os.environ['HOME'], organization, workspace, project_name)

    # os.makedirs(repo_folder_gh,exist_ok=True)

    #print('testapi Userable_GH: ')
    assert (Userable_GH())
    assert (Userable_GH(username_gh))
    #print('username_gh: '.rjust(twidth), end='')
    assert (Userable_GH(username_gh).getUsername_GH() == username_gh)
    #print(Userable_GH(username_gh).getUsername_GH())

if __name__ == "__main__":
    # execute as docker
    main()
