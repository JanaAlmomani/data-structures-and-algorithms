from StackAndQueue.queue import Queue
import pytest


def test_enqueue_single_value():
    q = Queue()
    q.enqueue(1)
    assert q.size == 1
    assert str(q) == "1 --> None"

def test_enqueue_multiple_values():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size == 3
    assert str(q) == "1 --> 2 --> 3 --> None"

def test_dequeue_single_value():
    q = Queue()
    q.enqueue(1)
    assert q.size == 1
    assert q.dequeue() == 1

def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.size == 0
    with pytest.raises(Exception):
        q.dequeue()

def test_peek():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1

def test_peek_empty_queue():
    q = Queue()
    with pytest.raises(Exception):
        q.peek()

def test_is_empty():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue(1)
    assert q.is_empty() == False
    q.dequeue()
    assert q.is_empty() == True
