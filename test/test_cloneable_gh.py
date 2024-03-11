import unittest
import os
import shutil
from able import Cloneable_GH

class TestCloneable(unittest.TestCase):

    def setUp(self):
        self.organization = 'test-org'
        self.username = 'wilfongjt'
        self.project_name = 'py_test'
        self.workspace = '00_clone'
        self.branch = 'clone_branch'
        # Create target folder
        ## home/Development/organization/workspace/project/branch/project
        self.repo_folder = '{}/Development/{}/{}/{}/{}/{}'.format(self.os.environ['HOME'],
                                                                  self.organization,
                                                                  self.workspace,
                                                                  self.project_name,
                                                                  self.branch,
                                                                  self.project_name)
        self.project_folder = '{}/Development/{}/{}/{}'.format(os.environ['HOME'],
                                                               self.organization,
                                                               self.workspace,
                                                               self.project_name)
        # print('repo_folder_gh   ', repo_folder_gh)
        # print('repo_folder_gh',repo_folder_gh)
        os.makedirs(self.project_folder, exist_ok=True)


    def test_init(self):
        class Example(Cloneable_GH):
            def __init__(self):
                Cloneable_GH.__init__(self)
        assert(Example())

    def tearDown(self):
        if os.path.isdir(self.project_folder):
            shutil.rmtree(self.project_folder)

if __name__ == '__main__':
    unittest.main()