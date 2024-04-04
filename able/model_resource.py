# deprecated
import os
import json
import able

class ResourceModel(dict):
    ##
    ##__ResourceModel__
    ##
    ## Dictionary that models github resource
    ##
    ##* load dictionary from github markdown document


    def __init__(self, md_string):
        #contents = {}
        stack = able.stack.Stack()

        line_list = md_string.split('\n')
        for ln in line_list:

            if ln.startswith('#'):
                stack.pop(count=(stack.size() - able.level.Level(ln)) + 1)
                stack.push(ln.replace('# ', '').replace('#', '').replace(':', ''))
                stack.update(self, {})

            elif ln.startswith('1.'):
                ln = ln.replace('1. ', '')
                ln = able.string_normal.NormalString(ln)
                s = ln.split(' : ', maxsplit=1)

                stack.push(s[0])
                if able.is_array.IsArray(s[1]):
                    s[1] = json.loads(able.string_json.JSONString(s[1]).replace('\'', '"'))
                elif able.is_object.IsObject(s[1]):
                    s[1] = json.loads(able.string_json.JSONString(s[1]).replace('\'', '"'))
                stack.update(self, s[1])
                stack.pop()


def main():
    from pprint import pprint
    from  string_reader import StringReader
    from string_template import TemplateString
    # handle default with github template
    md_project_string = str(os.getcwd()).replace('able','able/template/hapi/model/latest')
    print('A md_project_string',md_project_string)
    md_project_string = '{}/model.resource.md.C---.tmpl'.format(md_project_string)
    print('B md_project_string',md_project_string)
    md_project_string = StringReader(md_project_string)
    print('C md_project_string',md_project_string)

    nv_list = [{'name':'<<WS_ORGANIZATION>>', 'value':'testapi-org'},
               {'name':'<<GH_PROJECT>>', 'value':'able'},
               {'name':'<<WS_RESOURCE>>', 'value':'CRAZY'}]

    md_project_string = TemplateString(md_project_string, nv_list)
    print('D md_project_string',md_project_string)
    # handle template resource  values
    #md_project = str(os.getcwd()).replace('able','source/data')
    #md_project = '{}/model.lb_project.md'.format(md_project)
    #print('md_project', md_project)
    #md_string = StringReader(md_project)
    assert (ResourceModel('') == {})

    pprint(ResourceModel(md_project_string))

    assert(ResourceModel(md_project_string))
    assert(type(ResourceModel(md_project_string) is dict))

    # assert ('resource' in ResourceModel(md_project_string))
    pprint (ResourceModel(md_project_string)['CRAZY']['model'])
    #assert ('CRAZY' in ResourceModel(md_project_string)['CRAZY']['resource'])

    #pprint(ResourceModel(md_project_string))

if __name__ == "__main__":
    # execute as docker
    main()
