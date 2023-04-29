import pytest

from LinkedList.LinkedList import *

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    return ll


def test_empty_linked_list():
    linked_list = LinkedList()
    expected = "Empty LinkedList"
    actual = str(linked_list)
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

# Test append 
def test_append(ll):
    ll.append(5)
    expected = "{ 3 } -> { 2 } -> { 1 } -> { 5 } -> NULL"
    actual = str(ll)
    assert expected == actual
# Test insert after
def test_insert_after():
    # Create a linked list with three nodes: 1 -> 2 -> 3 -> NULL
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
# Test inserting after a node with value 3
    ll.insert_after(3, 5)
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 5 } -> NULL"
    assert str(ll) == expected

    # Test inserting after a node with value 2
    ll.insert_after(2, 5)
    assert str(ll) == "{ 1 } -> { 2 } -> { 5 } -> { 3 } -> { 5 } -> NULL"

    # Test inserting after a non-existent value
    with pytest.raises(ValueError):
        ll.insert_after(4, 5)
    assert str(ll) == "{ 1 } -> { 2 } -> { 5 } -> { 3 } -> { 5 } -> NULL"

def test_insert_before():
    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.to_string() == "NULL"
    
    linked_list.insert_before(3, 1)
    assert linked_list.to_string() == "NULL"
    
    linked_list.append(2)
    linked_list.insert_before(2, 1)
    assert linked_list.to_string() == "{ 1 } -> { 2 } -> NULL"
    
    linked_list.insert_before(1, 0)
    assert linked_list.to_string() == "{ 0 } -> { 1 } -> { 2 } -> NULL"


def test_kthFromEnd():
    # Test empty list
    linked_list = LinkedList()
    try:
        linked_list.kthFromEnd(0)
    except ValueError as e:
        assert str(e) == "List is empty"
    
    # Test k < 0
    try:
        linked_list.kthFromEnd(-1)
    except ValueError as e:
        assert str(e) == "k must be a positive integer"
    
    # Test k >= length of list
    linked_list.append(1)
    try:
        linked_list.kthFromEnd(1)
    except ValueError as e:
        assert str(e) == "k is greater than or equal to the length of the list"
    
    # Test k = 0
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list.kthFromEnd(0) == 3
    
    # Test general case
    assert linked_list.kthFromEnd(1) == 2
