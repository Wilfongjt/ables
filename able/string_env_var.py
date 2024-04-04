import os

class EnvVarString(str):
    def __new__(cls, keys=['GH_', 'WS_']):
        contents=''
        content_list = []
        for var in os.environ:
            for key in keys:
                if var.startswith(key):
                    content_list.append('{}={}'.format(var, os.environ[var]))
        if len(content_list) > 0:
            contents = '\n'.join(content_list)
        instance = super().__new__(cls, contents)
        return instance

def main():
    # no hits in environ
    assert (EnvVarString()=='')
    # add env var
    os.environ['GH_TEMP']='GH_TEMP'
    os.environ['GH_TEMP2']='GH_TEMP2'
    os.environ['WS_TEMP']='WS_TEMP'

    print(EnvVarString())
    assert (EnvVarString()=='GH_TEMP=GH_TEMP\nGH_TEMP2=GH_TEMP2\nWS_TEMP=WS_TEMP')



if __name__ == "__main__":
    # execute as docker
    main()