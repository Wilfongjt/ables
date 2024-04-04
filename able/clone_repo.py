from able import Cloneable_GH #Projectable #, Userable_GH , Urlable_GH, Branchable_GH

#class CloneRepo(Cloneable_GH,Projectable, Userable_GH, Urlable_GH,  Branchable_GH):
class CloneRepo(Cloneable_GH):

    def __init__(self, repo_folder, username_gh):
        #Projectable.__init__(self)
        #Userable_GH.__init__(self)
        #Urlable_GH.__init__(self)
        Cloneable_GH.__init__(self)
        #Branchable_GH.__init__(self)
        self.clone(repo_folder, username_gh)

def main():
    import os
    import shutil

    organization = 'testapi-org'
    username = 'wilfongjt'
    project_name = 'py_test'
    workspace = '00_clone'
    branch_name = 'clone_branch_test'
    # Create target repo_folder
    ## home/Development/organization/workspace/lb_project/branch/repo
    repo_folder = '{}/Development/{}/{}/{}/{}/{}'.format(os.environ['HOME'],
                                                              organization,
                                                              workspace,
                                                              project_name,
                                                              branch_name,
                                                              project_name)
    branch_folder='/'.join(repo_folder.split('/')[0:-1])
    project_folder='/'.join(repo_folder.split('/')[0:-2])

    os.makedirs(branch_folder,exist_ok=True)

    # Test
    assert (CloneRepo(repo_folder, username))
    assert (os.path.isdir(repo_folder))

    # remove target repo_folder and files
    if os.path.isdir(repo_folder):
        shutil.rmtree(project_folder)

if __name__ == "__main__":
    # execute as docker
    main()