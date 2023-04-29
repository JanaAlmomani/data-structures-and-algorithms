import pytest
from LinkedList.LinkedList import *

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    return ll

# Test empty linked list
def test_empty_linked_list():
    LL = LinkedList()
    expected = "Empty LinkedList"
    actual = str(LL)
    assert expected == actual

# Test insert 3 nodes
def test_insert(ll):

    expected = "{ 3 } -> { 2 } -> { 1 } -> NULL"
    actual = str(ll)
    assert expected == actual
    
# Test linked list to string
def test_to_string(ll):
    assert ll.to_string() == "{ 3 } -> { 2 } -> { 1 } -> NULL"

# Test includes 
def test_includes(ll):
    expected = "False"
    actual = str(ll.includes(9))
    assert expected == actual

# Test includes 
def test_includes_two(ll):
    assert ll.includes(1) == True
    assert ll.includes(2) == True
    assert ll.includes(3) == True
    assert ll.includes(4) == False

