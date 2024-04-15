
class Recorder(dict):
    def __init__(self):
        self['step_list'] = []
        self['step_list'].append({'msg': '[*]', 'count': 1})

    def add(self, msg, arrow='->'):

        msg = '{} {}'.format(arrow, msg)
        if msg == self['step_list'][-1]['msg']:
            self['step_list'][-1]['count'] += 1
        else:
            self['step_list'].append({'msg': msg, 'count': 1})

        return self

class DiagramString(str):

    def __new__(cls, recording=None):
        contents = recording
        if not recording:
            contents=''

        contents = ''
        if 'step_list' not in recording:
            recording['step_list'] = []

        for s in recording['step_list']:
            if s['count'] == 1:
                contents += ' {}'.format(s['msg'])
            else:
                contents += ' {} ({})'.format(s['msg'], s['count'])

        instance = super().__new__(cls, contents)
        return instance

def main():

    assert (Recorder()=={'step_list': [{'msg': '[*]', 'count': 1}]})
    assert (Recorder().add('A') == {'step_list': [{'msg': '[*]', 'count': 1}, {'msg': '-> A', 'count': 1}]})
    assert (Recorder().add('A').add('A') == {'step_list': [{'msg': '[*]', 'count': 1}, {'msg': '-> A', 'count': 2}]})
    assert (Recorder().add('A').add('A').add('B') == {'step_list': [{'msg': '[*]', 'count': 1}, {'msg': '-> A', 'count': 2}, {'msg': '-> B', 'count': 1}]})

if __name__ == "__main__":
    # execute as docker
    main()