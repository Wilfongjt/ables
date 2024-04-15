class Recordable():
    ##
    ##__Recordable__
    ##
    ##
    def __init__(self):
        self.recording = {}

    def addRecord(self, msg, arrow='->'):
        ##* Record github message on request

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

    def getRecording(self):
        return self.recording
    def getDiagram(self):
        ##* Retrieve recorded steps
        rc = ''
        if 'step_list' not in self.recording:
            self.recording['step_list'] = []

        for s in self.recording['step_list']:
            if s['count'] == 1:
                rc += ' {}'.format(s['msg'])
            else:
                rc += ' {} ({})'.format(s['msg'],s['count'])

        return rc.strip()
def main():

    # testapi
    expected={'step_list': [{'msg': '[*] -> A', 'count': 1}, {'msg': '-> B', 'count': 1}]}
    expected_diagram='[*] -> A -> B'

    assert(Recordable())
    assert(Recordable().addRecord('A').addRecord('B').getRecording()==expected)
    assert(Recordable().addRecord('A').addRecord('B').getDiagram()==expected_diagram)

    print(Recordable().addRecord('A').addRecord('B').addRecord('B').getRecording())
    print(Recordable().addRecord('A').addRecord('B').addRecord('B').getDiagram())

if __name__ == "__main__":
    # execute as docker
    main()