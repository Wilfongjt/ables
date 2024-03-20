import unittest
import os
import shutil
from able import State

class TestState(unittest.TestCase):

    def setUp(self):
        # setup
        self.folder = '{}/Development/Temp/state'.format(os.environ['HOME'])
        self.template_folder = '{}/template'.format(self.folder)
        self.template_hard_filename = '{}/template.txt.CRUD.tmpl'.format(self.template_folder)
        self.template_soft_filename = '{}/template.txt.crud.tmpl'.format(self.template_folder)
        self.template_dash_filename = '{}/template.txt.----.tmpl'.format(self.template_folder)

        self.target_folder = '{}/output'.format(self.folder)
        self.target_filename = '{}/template.txt'.format(self.target_folder)

        self.contents = '# ab\nA=<<A>>\nB=<<B>>'
        os.makedirs(self.template_folder, exist_ok=True)
        os.makedirs(self.target_folder, exist_ok=True)

        # create github template file to read
        with open(self.template_hard_filename, 'w') as f:
            f.write(self.contents)
        with open(self.template_soft_filename, 'w') as f:
            f.write(self.contents)
        with open(self.template_dash_filename, 'w') as f:
            f.write(self.contents)


    def test_init(self):

        assert (State(self.template_hard_filename, self.target_filename))
        #print (os.path.isfile(self.target_filename))
        assert (not State(self.template_hard_filename, self.target_filename).isTargetReadable())

        assert (State(self.template_hard_filename, self.target_filename).isHardCreate())
        assert (State(self.template_hard_filename, self.target_filename).isHardUpdate())
        assert (State(self.template_hard_filename, self.target_filename).isHardDelete())

        assert (not State(self.template_hard_filename, self.target_filename).isSoftCreate())
        assert (not State(self.template_hard_filename, self.target_filename).isSoftUpdate())
        assert (not State(self.template_hard_filename, self.target_filename).isSoftDelete())

        assert (not State(self.template_soft_filename, self.target_filename).isHardCreate())
        assert (not State(self.template_soft_filename, self.target_filename).isHardUpdate())
        assert (not State(self.template_soft_filename, self.target_filename).isHardDelete())

        assert (State(self.template_soft_filename, self.target_filename).isSoftCreate())
        assert (State(self.template_soft_filename, self.target_filename).isSoftUpdate())
        assert (State(self.template_soft_filename, self.target_filename).isSoftDelete())

        assert (not State(self.template_dash_filename, self.target_filename).isHardCreate())
        assert (not State(self.template_dash_filename, self.target_filename).isHardUpdate())
        assert (not State(self.template_dash_filename, self.target_filename).isHardDelete())

        assert (not State(self.template_dash_filename, self.target_filename).isSoftCreate())
        assert (not State(self.template_dash_filename, self.target_filename).isSoftUpdate())
        assert (not State(self.template_dash_filename, self.target_filename).isSoftDelete())


    def tearDown(self) -> None:
        # cleanup
        fileExists = os.path.isdir(self.folder)
        if fileExists:
            shutil.rmtree(self.folder)


if __name__ == '__main__':
    unittest.main()