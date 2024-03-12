import unittest
import os
import shutil
from able import NormalString

class TestState(unittest.TestCase):

    #def setUp(self):
    #    # setup

    def test_init(self):
        from pprint import pprint
        #print('normalize', NormalString('{name: hi, type: k}'))
        #print('normalize', NormalString('b: {name: hi, type: k}'))
        #print('normalize',
        #      NormalString('parameter: [token_id=TOKEN,owner_id=OWNERID,primary_key=PRIMARYKEY,trip=TRIPLE]'))
        #print('normalize',
        #      NormalString('{ name: james, type: [{name:w,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}'))
        assert (NormalString('{name: hi, type: k}') == '{ name : hi , type : k }')
        assert (NormalString('b: {name: hi, type: k}') == 'b : { name : hi , type : k }')
        assert (NormalString('parameter: [token_id=TOKEN,owner_id=OWNERID,primary_key=PRIMARYKEY,trip=TRIPLE]')
                == 'parameter : [ token_id=TOKEN , owner_id=OWNERID , primary_key=PRIMARYKEY , trip=TRIPLE ]')
        assert (NormalString('{ name: james, type: [{name:w,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}')
                == '{ name : james , type : [ { name : w , type : 2 } ] , kind : [ 1 , -1 , 2.0 , -2.00 , abc , { name : 1 } ] }')

    #def tearDown(self) -> None:
    #    # cleanup
    #    fileExists = os.path.isdir(self.repo_folder)
    #    if fileExists:
    #        shutil.rmtree(self.repo_folder)


if __name__ == '__main__':
    unittest.main()