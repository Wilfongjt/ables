
class Mergeable():
    ##
    ##__Mergable__
    ##
    ## Render a template with user provided values
    def __init__(self):
        self.merged_value = ''

    def create_instance(self):
        return Mergeable()

    def merge(self, nv_list):
        ##
        ##* Merge name-value pairs into a given template string on request
        # replace found names with values by iteration
        self.merged_value = ''
        if isinstance(self, str):
            self.merged_value = self
        for nv in nv_list:
            self.merged_value = self.merged_value.replace(nv['name'], nv['value'])

        return self.create_instance()

def main():
    t_str = '''
    NAME=<<NAME>>
    DATA=<<DATA>>
    '''.replace('  ','')
    expected = '''
    NAME=name
    DATA=data
    '''.replace('  ','')
    nv_list = [{'name': '<<NAME>>', 'value': 'name'},
               {'name': '<<DATA>>', 'value': 'data'}]
    assert(isinstance(Mergeable().merge(nv_list), Mergeable))
    print(Mergeable().merge(nv_list).merged_value)
    assert(Mergeable().merge(nv_list).merged_value == '') # nothing to merge into

    class Example(str, Mergeable):
        def __init__(self, string_value, nv_list=[]):
            Mergeable.__init__(self)
        def __new__(cls, string_value, nv_list=[]):
            merged_value=string_value
            for nv in nv_list:
                merged_value = merged_value.replace(nv['name'], nv['value'])

            instance = super().__new__(cls, merged_value)
            return instance

        def create_instance(self):
            return Example(self.merged_value)

    assert(Example(t_str)==t_str)
    assert(Example(t_str, nv_list)==expected)
    assert(Example(t_str).merge(nv_list)==expected)


if __name__ == "__main__":
    # execute as docker
    main()