#module level - runs once per module (file)
# use module level set up and tear down when you want to execute the set up and tear down once in the curent file
# setup_module -- only one per file
#setup_class() -- one per class
#setup_method() - one per class


import pytest
def setup_module(module):
    print("open the db connection")

def teardown_module( module):
    print("closing the db connection")

def test_read():
    print("Reading the db")

def test_write():
    print("writing the data to the db")

def test_updating():
    print("updating the data in db")




