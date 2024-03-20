import unittest
import os
import shutil
from able import Cloneable_GH

class TestCloneable(unittest.TestCase):

    def setUp(self):
        self.organization = 'testapi-org'
        self.username = 'wilfongjt'
        self.project_name = 'py_test'
        self.workspace = '00_clone'
        self.branch_name = 'clone_branch_test'
        # Create target repo_folder
        ## home/Development/organization/workspace/project/branch/repo
        self.repo_folder = '{}/Development/{}/{}/{}/{}/{}'.format(os.environ['HOME'],
                                                                  self.organization,
                                                                  self.workspace,
                                                                  self.project_name,
                                                                  self.branch_name,
                                                                  self.project_name)
        self.project_folder = '{}/Development/{}/{}/{}'.format(os.environ['HOME'],
                                                               self.organization,
                                                               self.workspace,
                                                               self.project_name)
        self.branch_folder = '{}/Development/{}/{}/{}/{}'.format(os.environ['HOME'],
                                                                  self.organization,
                                                                  self.workspace,
                                                                  self.project_name,
                                                                  self.branch_name)

        # print('repo_folder_gh   ', repo_folder_gh)
        # print('repo_folder_gh',repo_folder_gh)
        os.makedirs(self.branch_folder, exist_ok=True)


    def test_init(self):
        class Example(Cloneable_GH):
            def __init__(self):
                Cloneable_GH.__init__(self)
        assert(Example().clone(self.repo_folder,self.username))
        assert(os.path.isdir(self.repo_folder))

    def tearDown(self):
        if os.path.isdir(self.project_folder):
            shutil.rmtree(self.project_folder)

if __name__ == '__main__':
    unittest.main()