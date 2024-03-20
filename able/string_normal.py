
class NormalString(str):
    ##
    ##__NormalString__
    ##
    ## Normalize github JSON string for predictable spaces and symbols
    def __new__(cls, json_string):
        # .replace(';', ' ; ') \
        #                               .replace('!', ' ! ') \
        #                               .replace('(', ' ( ') \
        #                               .replace(')', ' ) ') \
        # .replace('"', ' " ') \
        #                               .replace('<', ' < ') \
        #                               .replace('>', ' > ') \
        #                               .replace(',', ' , ') \
        #                               .replace('?', ' ? ') \
        contents = json_string.replace(',', ' , ') \
                              .replace('{', ' { ') \
                              .replace('}', ' } ') \
                              .replace('[', ' [ ') \
                              .replace(']', ' ] ') \
                              .replace(':', ' : ') \
                              .replace('  ', ' ') \
                              .strip()

        contents = contents.replace('  ', ' ') # once just isnt enough
        #contents = contents.replace('{ ', "{'").replace(' :', "': ").replace(' , '," , '")

        instance = super().__new__(cls, contents)
        return instance


def main():
    from pprint import pprint
    print('normalize', NormalString('{name: hi, type: k}'))
    print('normalize', NormalString('docker: {name: hi, type: k}'))
    print('normalize',NormalString('parameter: [token_id=TOKEN,owner_id=OWNERID,primary_key=PRIMARYKEY,trip=TRIPLE]'))
    print('normalize',NormalString('{ name: james, type: [{name:w,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}'))
    assert(NormalString('{name: hi, type: k}')=='{ name : hi , type : k }')
    assert(NormalString('docker: {name: hi, type: k}')=='docker : { name : hi , type : k }')
    assert(NormalString('parameter: [token_id=TOKEN,owner_id=OWNERID,primary_key=PRIMARYKEY,trip=TRIPLE]')
                        == 'parameter : [ token_id=TOKEN , owner_id=OWNERID , primary_key=PRIMARYKEY , trip=TRIPLE ]')
    assert(NormalString('{ name: james, type: [{name:w,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}')
                        == '{ name : james , type : [ { name : w , type : 2 } ] , kind : [ 1 , -1 , 2.0 , -2.00 , abc , { name : 1 } ] }')

    print('normalize', NormalString('{name: hi, type: k!s}'))
    print(NormalString('parameter: [token_id=TOKEN,owner_id:OWNERID,primary_key:PRIMARYKEY]'))

if __name__ == "__main__":
    # execute as docker
    main()
    # mainProjectScript()