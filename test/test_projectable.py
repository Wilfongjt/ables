import os
import unittest
import shutil

from able import Projectable

class TestProjectable(unittest.TestCase):
    def setUp(self) -> None:
        # setup
        self.repo_folder = '{}/Development/client/workspace/lb_project/clone/repo'.format(os.environ['HOME'])
        os.makedirs(self.repo_folder, exist_ok=True)
        self.project_name = 'lb_project'

    def test_init(self):
        class Example(Projectable):
            def __init__(self):
                Projectable.__init__(self)

        assert (Example().setRepoFolder(self.repo_folder)
                .getRepoFolder() == self.repo_folder)
        assert (Example().setRepoFolder(self.repo_folder)
                .getWorkspaceFolder() == '{}/Development/client/workspace'.format(
            os.environ['HOME']))
        assert (Example().setRepoFolder(self.repo_folder)
                .getClientFolder() == '{}/Development/client'.format(
            os.environ['HOME']))
        assert (Example().setRepoFolder(self.repo_folder)
                .getDevelopmentFolder() == '{}/Development'.format(
            os.environ['HOME']))

        assert (Example().setRepoFolder(self.repo_folder).getRepoName() == 'repo')

    def tearDown(self) -> None:
        # tearDown
        if os.path.isdir('{}'.format(self.repo_folder)):
            shutil.rmtree(self.repo_folder)

if __name__ == '__main__':
    unittest.main()