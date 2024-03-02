from able import Mergeable
# Deprecated
class MergerString(str, Mergeable):
    ##
    ##__MergerString__ Deprecated, use TempalteString instead
    ##
    ##
    def __init__(self, string_value, nv_list=None):
        Mergeable.__init__(self)

    def __new__(cls, string_value, nv_list=None):
        ##
        ##* Merge many name-value pairs into a given template string on initiation
        # replace found names with values by iteration
        contents=string_value
        if nv_list:
            for nv in nv_list:
                contents = contents.replace(nv['name'], nv['value'])

        instance = super().__new__(cls, contents)
        return instance

    def create_instance(self):
        return MergerString(self.merged_value)

def main():
    t_str = 'A=<<A>>, B=<<B>>'
    expected = 'A=a, B=b'
    nv_list = [{'name': '<<A>>', 'value': 'a'},
               {'name':'<<B>>', 'value': 'b'}]
    assert (MergerString(t_str))
    assert (MergerString(t_str)==t_str)
    assert (MergerString(t_str, nv_list)==expected)
    assert (MergerString(t_str).merges(nv_list)==expected)

if __name__ == "__main__":
    # execute as docker
    main()
