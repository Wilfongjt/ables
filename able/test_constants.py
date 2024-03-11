import os

class TestConstants():
    def __init__(self):
        self.organization = 'test-org'
        self.username_gh = 'test-user'
        self.project_name = 'py_test'
        self.project_folder = '{}/Development/{}'.format(os.environ['HOME'])
        self.data=[
            [{'name': 'A', 'value': 'a'}, {'name': 'B', 'value': 'b'}]
        ]
        self.nv_list = [{'name':'<<WS_ORGANIZATION>>', 'value':'test-org'},
                        {'name':'<<GH_PROJECT>>', 'value':'able'},
                        {'name':'<<WS_RESOURCE>>', 'value':'CRAZY'}]