import os
import unittest
import shutil

from able import ProjectModel, StringReader

class TestProjectModel(unittest.TestCase):

    def setUp(self):
        self.md_project = str(os.getcwd()).replace('testapi', 'able/template/hapi/model/latest/model.lb_project.md.C---.tmpl')
        # print('mfz-lb_project', self.md_project)

        # md_project = '{}/model.lb_project.md'.format(md_project)
        # print('isfile', os.path.isfile(self.md_project))
        self.md_string = StringReader(self.md_project)
        # print('md_string', self.md_string)

    def test_init(self):
        # testapi
        assert (ProjectModel('')=={})
        # print (ProjectModel(self.md_string))

        assert (ProjectModel(self.md_string))
        assert (type(ProjectModel(self.md_string) is dict))
        assert ('lb_project' in ProjectModel(self.md_string))
        assert ('audience' in ProjectModel(self.md_string)['lb_project'])
        assert ('claim' in ProjectModel(self.md_string)['lb_project'])
        assert ('issuer' in ProjectModel(self.md_string)['lb_project'])
        assert ('name' in ProjectModel(self.md_string)['lb_project'])
        assert ('owner' in ProjectModel(self.md_string)['lb_project'])
        assert ('resource' in ProjectModel(self.md_string)['lb_project'])
        assert ('subject' in ProjectModel(self.md_string)['lb_project'])

    #def tearDown(self):
    #    fileExists = os.path.isfile(self.folder_filename)
    #    if fileExists:
    #        shutil.rmtree(self.repo_folder)

if __name__ == '__main__':
    unittest.main()