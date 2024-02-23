import os
import unittest
import shutil

#from able import ProjectModel #, StringReader

class TestProjectModel(unittest.TestCase):

    def setUp(self):
        md_project = str(os.getcwd()).replace('able', 'source/data')
        md_project = '{}/model.project.md'.format(md_project)
        print('md_project', md_project)
        #self.md_string = StringReader(md_project)

    def test_init(self):
        # test
        assert (ProjectModel('')==0)
        #assert (ProjectModel('abc')==0)
        #assert (ProjectModel('# abc') == 1)
        #assert (ProjectModel('## abc') == 2)
        #assert (ProjectModel('### abc') == 3)
        #assert (ProjectModel('### # abc') == 3)

    #def tearDown(self):
    #    fileExists = os.path.isfile(self.folder_filename)
    #    if fileExists:
    #        shutil.rmtree(self.folder)

if __name__ == '__main__':
    unittest.main()