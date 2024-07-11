# from able import Mergeable
from able import Mergeable

class TemplateString(str, Mergeable):
    ##
    ##__TemplateString__
    ##
    ## String with github merge function
    ##
    def __init__(self, template, nv_list=[]):
        Mergeable.__init__(self)

    def __new__(cls, template, nv_list=[]):
        ##* merge nv_list into string on instantiation
        contents=[]
        for ln in str(template).split('\n'):
            for nv in nv_list:
                if nv['name'] in ln:
                    ln = ln.replace(nv['name'],'{}'.format(nv['value']))
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
    MAX=<<MAX>>
    '''.replace('  ','')
    expected1 = '''
        NAME=<<NAME>>
        DATA=data
        MAX=<<MAX>>
        '''.replace('  ', '')
    expected2 = '''
    NAME=name
    DATA=data
    MAX=0
    '''.replace('  ','')
    nv_list = [{'name': '<<NAME>>', 'value': 'name'},
               {'name': '<<DATA>>', 'value': 'data'},
               {'name': '<<MAX>>', 'value': 0}]
    # initialize
    assert(TemplateString(t_str)==t_str)
    # imeadiate templatization
    print('templateString', TemplateString(t_str).merge('<<DATA>>','data'))
    assert(TemplateString(t_str).merge('<<DATA>>','data')==expected1) # delay templatization
    assert(TemplateString(t_str).merges(nv_list)==expected2) # delay templatization
    # delay templatization
    assert(TemplateString(t_str, nv_list)==expected2) # immeadiate templatization


if __name__ == "__main__":
    # execute as docker
    main()