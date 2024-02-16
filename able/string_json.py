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

            is_val = i > 0 and contents[i - 1] == ':'

            if is_val and bool_pattern.match(item):
                ##* convert boolean string value to boolean actual
                contents[i] = "{}".format(item)
            elif re.match(key_pattern, item):
                ##* collect key
                contents[i] = "'{}'".format(item)
            elif re.match(num_pattern, item):
                ##* convert string number value to number actual
                contents[i] = "{}".format(item)
            elif is_val and item not in ['[','{']:
                contents[i] = "'{}'".format(item)
            else:
                if len(item)>1:
                    contents[i]="'{}'".format(item)
                #else:
                #    print('else ok',item )
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
    #print (JSONString(NormalString('{ name: james, type: [{name:w,type:x}]}')))
    #print("{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 'x' } ] }")
    assert(JSONString(NormalString('{ name: james, type: [{name:w,type:x}]}')) == "{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 'x' } ] }")
    assert(JSONString(NormalString('{ name: james, type: [{name:w,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}'))=="{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 2 } ] , 'kind' : [ 1 , -1 , 2.0 , -2.00 , 'abc' , { 'name' : 1 } ] }")
    assert(JSONString(NormalString('{ name: james, type: [{name:w,type:2},{name:x,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}'))
           == "{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 2 } , { 'name' : 'x' , 'type' : 2 } ] , 'kind' : [ 1 , -1 , 2.0 , -2.00 , 'abc' , { 'name' : 1 } ] }")
    assert(JSONString(NormalString('{ name: james, is:True, isnt: False}'))=="{ 'name' : 'james' , 'is' : True , 'isnt' : False }")
    assert( JSONString(NormalString('parameter: [token_id=TOKEN,owner_id=OWNERID,primary_key=PRIMARYKEY]')) == "'parameter' : [ 'token_id=TOKEN' , 'owner_id=OWNERID' , 'primary_key=PRIMARYKEY' ]")
    assert( JSONString(NormalString('parameter: [{token_id:TOKEN},{owner_id:OWNERID,primary_key:{name:PRIMARYKEY}}]'))=="'parameter' : [ { 'token_id' : 'TOKEN' } , { 'owner_id' : 'OWNERID' , 'primary_key' : { 'name' : 'PRIMARYKEY' } } ]")

if __name__ == "__main__":
    # execute as docker
    main()
    # mainProjectScript()