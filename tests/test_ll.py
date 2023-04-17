import pytest
from LinkedList.LinkedList import *


# Test empty linked list
def test_empty_ll():
    ll = LinkedList()
    expected = "Empty LinkedList"
    actual = str(ll)
    assert expected == actual

# Test insert 6 nodes
def test_insert(ll):
    expected = "{ 9 } -> { 6 } -> { 1 } -> { 2 } -> { 5 } -> { 3 } -> NULL"
    actual = str(ll)
    assert expected == actual

# Test includes 
def test_includes(ll):
    expected = "True"
    actual = str(ll.includes(9))
    assert expected == actual

# Test append 
def test_append(ll):
    ll.append(20)
    expected = "{ 9 } -> { 6 } -> { 1 } -> { 2 } -> { 5 } -> { 3 } -> { 20 } -> NULL"
    actual = str(ll)
    assert expected == actual

# Test insert_before
def test_insert_before(ll):
    ll.insert_before(6, 4)
    expected = "{ 9 } -> { 4 } -> { 6 } -> { 1 } -> { 2 } -> { 5 } -> { 3 } -> NULL"
    assert str(ll) == expected

# Test insert_before not found
def test_insert_before_not_found(ll):
    ll.insert_before(8, 4)
    expected = "{ 9 } -> { 6 } -> { 1 } -> { 2 } -> { 5 } -> { 3 } -> NULL"
    assert str(ll) == expected

# Test insert_before 
def test_insert_after(ll):
    ll.insert_after(6, 4)
    expected = "{ 9 } -> { 6 } -> { 4 } -> { 1 } -> { 2 } -> { 5 } -> { 3 } -> NULL"
    assert str(ll) == expected

# Test insert_before not found
def test_insert_after_not_found(ll):
    ll.insert_after(8, 4)
    expected = "{ 9 } -> { 6 } -> { 1 } -> { 2 } -> { 5 } -> { 3 } -> NULL"
    assert str(ll) == expected

# { 9 } -> { 6 } -> { 1 } -> { 2 } -> { 5 } -> { 3 } -> NULL
@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(5)
    ll.insert(2)
    ll.insert(1)
    ll.insert(6)
    ll.insert(9)
    # ll.includes(9)
  
    return ll
