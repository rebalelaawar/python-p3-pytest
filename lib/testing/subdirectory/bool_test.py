#!/usr/bin/env python3

from bool_functions import return_true

def test_return_true():
    '''in bool_functions, function "return_true" returns True.'''
    result = return_true()
    assert result == True
    return result 
