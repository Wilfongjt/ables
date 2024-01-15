# from able import Mergeable
from able import Mergeable

class TemplateString(str, Mergeable):

    def __init__(self, template, nv_list=[]):
        Mergeable.__init__(self)

    def __new__(cls, template, nv_list=[]):
        contents=[]
        for ln in str(template).split('\n'):
            for nv in nv_list:
                if nv['name'] in ln:
                    ln = ln.replace(nv['name'],nv['value'])
            contents.append(ln)
        contents = '\n'.join(contents)
        instance = super().__new__(cls, contents)
        return instance

    def create_instance(self):
        return TemplateString(self.merged_value)


def main():
    t_str = '''
    NAME=<<NAME>>
    DATA=<<DATA>>
    '''.replace('  ','')
    expected1 = '''
        NAME=<<NAME>>
        DATA=data
        '''.replace('  ', '')
    expected2 = '''
    NAME=name
    DATA=data
    '''.replace('  ','')
    nv_list = [{'name': '<<NAME>>', 'value': 'name'},
               {'name': '<<DATA>>', 'value': 'data'}]
    # initialize
    assert(TemplateString(t_str)==t_str)
    # imeadiate templatization
    assert(TemplateString(t_str).merge('<<DATA>>','data')==expected1) # delay templatization
    assert(TemplateString(t_str).merges(nv_list)==expected2) # delay templatization
    # delay templatization
    assert(TemplateString(t_str, nv_list)==expected2) # immeadiate templatization


if __name__ == "__main__":
    # execute as docker
    main()