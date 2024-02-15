import re
import json

class JSONString(str):
    def __new__(cls, normal_string):
        key_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
        num_pattern = r'^[-0-9][0-9\.]*$'
        bool_pattern = re.compile(r'^(?:True|False)$')

        contents = normal_string.split(' ')
        i = 0
        for item in contents:

            if bool_pattern.match(item):
                contents[i] = "{}".format(item)
            elif re.match(key_pattern, item):
                contents[i] = "'{}'".format(item)
            elif re.match(num_pattern, item):
                contents[i] = "{}".format(item)

            i += 1
        contents = ' '.join(contents)

        instance = super().__new__(cls, contents)
        return instance

def main():
    from able.string_normal import NormalString

    #print(JSONString(NormalString('{ name: james, type: [{name:w,type:x}]}')))
    #print(JSONString(NormalString('{ name: james, type: [{name:w,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}')))
    #print(JSONString(NormalString('{ name: james, type: [{name:w,type:2},{name:x,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}')))
    #print(JSONString(NormalString('{ name: james, is:True, isnt: False}')))

    assert(JSONString(NormalString('{ name: james, type: [{name:w,type:x}]}'))=="{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 'x' } ] }")
    assert(JSONString(NormalString('{ name: james, type: [{name:w,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}'))=="{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 2 } ] , 'kind' : [ 1 , -1 , 2.0 , -2.00 , 'abc' , { 'name' : 1 } ] }")
    assert(JSONString(NormalString('{ name: james, type: [{name:w,type:2},{name:x,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}'))
           == "{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 2 } , { 'name' : 'x' , 'type' : 2 } ] , 'kind' : [ 1 , -1 , 2.0 , -2.00 , 'abc' , { 'name' : 1 } ] }")
    assert(JSONString(NormalString('{ name: james, is:True, isnt: False}'))=="{ 'name' : 'james' , 'is' : True , 'isnt' : False }")

if __name__ == "__main__":
    # execute as docker
    main()
    # mainProjectScript()