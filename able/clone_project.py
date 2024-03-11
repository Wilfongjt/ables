from able import Projectable, Userable_GH , Urlable_GH #, Cloneable_GH, Branchable_GH

class CloneProject(Projectable, Userable_GH, Urlable_GH, Cloneable_GH, Branchable_GH):
    def __init__(self, repo_folder=None, username_gh=None):
        Projectable.__init__(self)
        Userable_GH.__init__(self)
        Urlable_GH.__init__(self)
        Cloneable_GH.__init__(self)
        Branchable_GH.__init__(self)

        if repo_folder:
            #print('CloneProject repo_folder_gh', repo_folder_gh)
            self.setRepoFolder(repo_folder)
        if username_gh:
            #print('CloneProject 1 username_gh', username_gh)
            self.setUsername_GH(username_gh)
            #print('CloneProject 2 username_gh', self.getUsername_GH())
