import os
import shutil

class Recordable():
    ##
    ##__Recordable__
    ##
    ##
    def __init__(self):
        self.recording = {}
    def addStep(self, msg, arrow='->'):
        ##* Record a message

        if 'step_list' not in self.recording:
            self.recording['step_list'] = []

        if len(self.recording['step_list']) == 0:
            msg = '[*] -> {}'.format(msg)
            self.recording['step_list'].append({'msg': msg, 'count': 1})
        else:
            msg = '{} {}'.format(arrow, msg)
            if msg == self.recording['step_list'][-1]['msg']:
                self.recording['step_list'][-1]['count'] += 1
            else:
                self.recording['step_list'].append({'msg': msg, 'count': 1})

        return self

    def getSteps(self):
        ##* Retrieve recorded step
        rc = ''
        if 'step_list' not in self.recording:
            self.recording['step_list'] = []

        for s in self.recording['step_list']:
            if s['count'] == 1:
                rc += '{}'.format(s['msg'])
            else:
                rc += '{} ({})'.format(s['msg'],s['count'])

        return rc

    def formulate(self, form, title=None):
        ##* Convert JSON Object to String
        ##* eg {a:1, b:2} to (a, b)
        keys = []
        for key in form:
            keys.append(key)
        if title:
            return '({}({}))'.format(title, ','.join(keys))

        return '({})'.format(','.join(keys))


    def set_(self, key, value):
        if 'state' not in self.recording:
            self.recording['state'] = {}

        self.recording['state'][key] = value
        return self

    def get_(self, key=None):
        rc = None
        if 'state' not in self.recording:
            self.recording['state'] = {}

        if not key:
            rc = self.recording['state']
        elif key in self.recording['state']:
            rc = self.recording['state'][key]

        return rc

    def showSteps(self):
        print(self.getSteps())
        return self


def main():
    # setup
    folder = '{}/Development/client/workspace/project'.format(os.environ['HOME'])
    expected = '{}/Development/client'.format(os.environ['HOME'])
    project_name = 'project'
    os.makedirs(folder, exist_ok=True)

    #print('folder', folder)
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