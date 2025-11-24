import pytest
from Informatics_Lab3_Task1 import idsearch

def test1():
    
    result = idsearch()
    assert "root" in result

def test2():
    
    result = idsearch()
    assert isinstance(result, list)

def test3():

    result = idsearch()
    for item in result:
        assert isinstance(item, str)

def test4():
    result = idsearch()

    assert len(result) == len(set(result))

def temast5():
    result = idsearch()

    for id_value in result:
        assert not any(char in id_value for char in [' ', '"', "'", '<', '>'])
        assert len(id_value) > 0