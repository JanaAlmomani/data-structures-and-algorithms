from StackAndQueue.PseudoQueue import *
import pytest

def test_pseudoqueue():
    q = PseudoQueue()

    # Test enqueue method
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert str(q) == 'None <-- 30 <-- 20 <-- 10'

    # Test dequeue method
    assert q.dequeue() == 10
    assert q.dequeue() == 20
    assert str(q) == 'None <-- 30'

    # Test is_empty method
    assert not q.is_empty()
    q.dequeue()
    assert q.is_empty()

    # Test dequeue method on empty queue
    try:
        q.dequeue()
        assert False, "Expected an IndexError"
    except IndexError:
        pass

    # Test __str__ method on empty queue
    assert str(q) == "Empty PseudoQueue"
