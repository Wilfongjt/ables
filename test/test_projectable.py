import os
import unittest
import shutil

from able import Projectable

class TestProjectable(unittest.TestCase):
    def setUp(self) -> None:
        # setup
        self.folder = '{}/Development/client/workspace/project'.format(os.environ['HOME'])
        os.makedirs(self.folder, exist_ok=True)

    def test_init(self):
        class Example(Projectable):
            def __init__(self):
                Projectable.__init__(self)

        assert (Example().setProjectFolder(self.folder)
                .getProjectFolder() == self.folder)
        assert (Example().setProjectFolder(self.folder)
                .getWorkspaceFolder() == '{}/Development/client/workspace'.format(
            os.environ['HOME']))
        assert (Example().setProjectFolder(self.folder)
                .getClientFolder() == '{}/Development/client'.format(
            os.environ['HOME']))
        assert (Example().setProjectFolder(self.folder)
                .getDevelopmentFolder() == '{}/Development'.format(
            os.environ['HOME']))

    def tearDown(self) -> None:
        # tearDown
        if os.path.isdir('{}'.format(self.folder)):
            shutil.rmtree(self.folder)

if __name__ == '__main__':
    unittest.main()