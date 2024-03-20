import os

class TestConstants():
    def __init__(self):
        self.organization = 'testapi-org'
        self.username_gh = 'testapi-user'
        self.project_name = 'py_test'
        self.project_folder = '{}/Development/{}'.format(os.environ['HOME'])
        self.data=[
            [{'name': 'A', 'value': 'github'}, {'name': 'B', 'value': 'docker'}]
        ]
        self.nv_list = [{'name':'<<WS_ORGANIZATION>>', 'value':'testapi-org'},
                        {'name':'<<GH_PROJECT>>', 'value':'able'},
                        {'name':'<<WS_RESOURCE>>', 'value':'CRAZY'}]