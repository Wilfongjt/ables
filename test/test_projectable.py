import os
import unittest
import shutil

from able import Projectable

class TestProjectable(unittest.TestCase):
    def setUp(self) -> None:
        # setup
        self.folder = '{}/Development/client/workspace/project'.format(os.environ['HOME'])
        os.makedirs(self.folder, exist_ok=True)
        self.project_name = 'project'

    def test_init(self):
        class Example(Projectable):
            def __init__(self):
                Projectable.__init__(self)

        assert (Example().setRepoFolder(self.folder)
                .getRepoFolder() == self.folder)
        assert (Example().setRepoFolder(self.folder)
                .getWorkspaceFolder() == '{}/Development/client/workspace'.format(
            os.environ['HOME']))
        assert (Example().setRepoFolder(self.folder)
                .getClientFolder() == '{}/Development/client'.format(
            os.environ['HOME']))
        assert (Example().setRepoFolder(self.folder)
                .getDevelopmentFolder() == '{}/Development'.format(
            os.environ['HOME']))

        assert (Example().setRepoFolder(self.folder).getRepoName() == self.project_name)

    def tearDown(self) -> None:
        # tearDown
        if os.path.isdir('{}'.format(self.folder)):
            shutil.rmtree(self.folder)

if __name__ == '__main__':
    unittest.main()