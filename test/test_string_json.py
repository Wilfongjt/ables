import unittest
import os
import shutil
from able import NormalString, JSONString


class TestState(unittest.TestCase):

    #def setUp(self):
    #    # setup

    def test_init(self):
        #from pprint import pprint
        assert (JSONString(NormalString(
            '{ name: james, type: [{name:w,type:x}]}')) == "{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 'x' } ] }")
        assert (JSONString(NormalString(
            '{ name: james, type: [{name:w,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}')) == "{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 2 } ] , 'kind' : [ 1 , -1 , 2.0 , -2.00 , 'abc' , { 'name' : 1 } ] }")
        assert (JSONString(NormalString(
            '{ name: james, type: [{name:w,type:2},{name:x,type:2}], kind:[1, -1, 2.0, -2.00, abc, {name:1}]}'))
                == "{ 'name' : 'james' , 'type' : [ { 'name' : 'w' , 'type' : 2 } , { 'name' : 'x' , 'type' : 2 } ] , 'kind' : [ 1 , -1 , 2.0 , -2.00 , 'abc' , { 'name' : 1 } ] }")
        assert (JSONString(NormalString(
            '{ name: james, is:True, isnt: False}')) == "{ 'name' : 'james' , 'is' : True , 'isnt' : False }")

    #def tearDown(self) -> None:
    #    # cleanup
    #    fileExists = os.path.isdir(self.repo_folder)
    #    if fileExists:
    #        shutil.rmtree(self.repo_folder)


if __name__ == '__main__':
    unittest.main()