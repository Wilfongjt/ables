import os
import shutil

class Projectable():
    ##__Projectable__
    ##
    ##* project folder eg Development/client/workspace/project

    def __init__(self, project_folder=None):
        self.project_folder=project_folder

    def setProjectFolder(self, project_folder):
        ##* set project folder on request
        self.project_folder = project_folder
        return self

    def getProjectName(self):
        ##* retrive the GitHub project name from the project_folder
        return self.project_folder.split('/')[-1]

    def getDevelopmentFolder(self):
        ##__Enable reference to the development folder__
        ##* get "Development" folder on request
        ws = '/'.join(self.project_folder.split('/')[0:-3])
        return ws

    def getClientFolder(self):
        ##__Enable reference to the client folder__
        ##* get client folder on request
        ws = '/'.join(self.project_folder.split('/')[0:-2])
        return ws

    def getWorkspaceFolder(self):
        ## __Enable reference to the workspace folder__
        ##* get workspace folder on request
        return '/'.join(self.project_folder.split('/')[0:-1])

    def getProjectFolder(self):
        ##__Enable setting and reference to project folder__
        ##* get project folder on request
        ws = '/'.join(self.project_folder.split('/'))
        return ws

def main():
    # setup
    folder = '{}/Development/client/workspace/project'.format(os.environ['HOME'])
    expected = '{}/Development/client'.format(os.environ['HOME'])
    project_name = 'project'
    os.makedirs(folder, exist_ok=True)

    # test
    class Example(Projectable):
        def __init__(self):
            Projectable.__init__(self)

    assert (Example().setProjectFolder(folder).getProjectFolder()==folder)
    assert (Example().setProjectFolder(folder).getWorkspaceFolder()=='{}/Development/client/workspace'.format(os.environ['HOME']))
    assert (Example().setProjectFolder(folder).getClientFolder()=='{}/Development/client'.format(os.environ['HOME']))
    assert (Example().setProjectFolder(folder).getDevelopmentFolder()=='{}/Development'.format(os.environ['HOME']))

    assert (Example().setProjectFolder(folder).getProjectName()==project_name)

    # tearDown
    if os.path.isdir('{}'.format(folder)):
        shutil.rmtree(folder)


if __name__ == "__main__":
    # execute as docker
    main()