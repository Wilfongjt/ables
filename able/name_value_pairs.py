
#class ThisRow(str):
#class ThatValue(str):
from able.string_key import KeyString
from able.string_value import ValueString

class NameValuePairs(list):
    def __init__(self, multi_line_string='', break_on='='):
        # use cases
        # A         -> [{name:A, value:A}]
        # A\nB      -> [{name:A, value:A}, {name:B, value:B}]
        # A=a\nB=b  -> [{name:A=, value:a}, {name:B=, value:b}]
        # A\nB=b    -> [{name:A, value:A}, {name:B=, value:b}]

        if multi_line_string:
            multi_line_string = multi_line_string.split('\n')
            for item in multi_line_string:
                # item = item.split(break_on)
                self.append({'name': KeyString(item, break_on), 'value': ValueString(item, break_on)})
                if break_on in item:
                    self[-1]['op']=break_on
                '''
                if len(item) > 1:
                    # A=a
                    # A=a\nB=b
                    self.append({'name': KeyString(item, break_on), 'value': ValueString(item, break_on), 'op': break_on})
                    # self.append({'name': '{}{}'.format(item[0], break_on), 'value': '{}{}{}'.format(item[0],break_on,item[1])})
                    # self.append({'name': '{}{}'.format(item[0], break_on), 'value': '{}{}{}'.format(item[0],break_on,item[1])})
                else: #
                    if item[0]!='':
                        # A
                        # A\nB
                        self.append({'name': item[0], 'value': item[0]})
                '''
        # print('name value pairs', self)

def main():
    # DONT USE '==='  this doesnt work ... too confusing on the front end
    # print('name value pairs',NameValuePairs())
    assert(NameValuePairs() == [])
    assert(NameValuePairs('') == [])
    assert(NameValuePairs(None) == [])

    assert(NameValuePairs('A B') == [{'name': 'A B', 'value': 'A B'}])
    assert(NameValuePairs('A B\nC D') == [{'name': 'A B', 'value': 'A B'}, {'name': 'C D', 'value': 'C D'}])
    # print(NameValuePairs('A=B'))
    assert(NameValuePairs('A=B') == [{'name': 'A=', 'value': 'A=B', 'op': '='}])

    assert(NameValuePairs('A=B\nC D') == [{'name': 'A=', 'value': 'A=B', 'op': '='}, {'name': 'C D', 'value': 'C D'}])
    assert(NameValuePairs('A=B\nC=D') == [{'name': 'A=', 'value': 'A=B', 'op': '='}, {'name': 'C=', 'value': 'C=D', 'op': '='}])

if __name__ == "__main__":
    # execute as docker
    main()