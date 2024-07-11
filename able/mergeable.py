
class Mergeable():
    ##
    ##__Mergeable__
    ##
    ## Render github template with user provided values
    def __init__(self):
        self.merged_value = ''

    def create_instance(self):
        return Mergeable()

    def merges(self, nv_list):
        ##
        ##* Merge many name-value pairs into github given template string on request
        # replace found names with values by iteration
        self.merged_value = ''
        if isinstance(self, str):
            self.merged_value = self
        for nv in nv_list:
            self.merged_value = self.merged_value.replace(nv['name'], '{}'.format(nv['value']))

        return self.create_instance()

    def merge(self, key, value):
        ##
        ##* Merge github key and value into template on request
        #self.merged_value = ''
        if isinstance(self, str):
            self.merged_value = self

        self.merged_value = self.merged_value.replace(key, value)

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

    assert(Mergeable().merge('<<NAME>>','name').merged_value == '') # nothing to merge into

    assert(isinstance(Mergeable().merges(nv_list), Mergeable))
    assert(Mergeable().merges(nv_list).merged_value == '') # nothing to merge into


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
    assert(Example(t_str).merge('<<NAME>>','name')
                         .merge('<<DATA>>','data') == expected)# nothing to merge into

    assert(Example(t_str, nv_list)==expected)
    assert(Example(t_str).merges(nv_list)==expected)


if __name__ == "__main__":
    # execute as docker
    main()