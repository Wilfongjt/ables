import os

class EnvVarString(str):
    def __new__(cls, keys=['GH_', 'WS_'], recorder=None):
        contents=''
        content_list = []
        for var in os.environ:
            for key in keys:
                if var.startswith(key):
                    if recorder: recorder.add('var')
                    content_list.append('{}={}'.format(var, os.environ[var]))
        if len(content_list) > 0:
            contents = '\n'.join(content_list)
        instance = super().__new__(cls, contents)
        return instance

def main():
    from able import Recorder
    # no hits in environ
    recorder=Recorder()
    assert (EnvVarString(recorder=recorder)=='')
    # add env var
    os.environ['GH_TEMP']='GH_TEMP'
    os.environ['GH_TEMP2']='GH_TEMP2'
    os.environ['WS_TEMP']='WS_TEMP'

    print(EnvVarString(recorder=recorder))
    assert (EnvVarString(recorder=recorder)=='GH_TEMP=GH_TEMP\nGH_TEMP2=GH_TEMP2\nWS_TEMP=WS_TEMP')
    print('recorder', recorder)


if __name__ == "__main__":
    # execute as docker
    main()