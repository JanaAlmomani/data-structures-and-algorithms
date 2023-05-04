from StackAndQueue.stack import Stack
import pytest

def test_instantiate_empty_stack():
    stack = Stack()
    assert stack.size == 0

def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()

def test_peek_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()

def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()


def test_push_single_value():
    stack = Stack()
    stack.push(1)
    assert stack.size == 1
    assert stack.top.value == 1

def test_push_multiple_values():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size == 3
    assert stack.top.value == 3

def test_pop_multiple_value():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.peek() == 1


def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False
    stack.pop()
    assert stack.is_empty() == True






