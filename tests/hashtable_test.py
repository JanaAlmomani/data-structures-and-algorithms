import pytest
from hashtable.hashtable.hashtable import *

def test_set_get():
    ht = HashTable()
    ht.set('key1', 'value1')
    ht.set('key2', 'value2')
    ht.set('key3', 'value3')
    assert ht.get('key1') == 'value1'
    assert ht.get('key2') == 'value2'
    assert ht.get('key3') == 'value3'

def test_set_replace():
    ht = HashTable()
    ht.set('key', 'value1')
    ht.set('key', 'value2')
    assert ht.get('key') == 'value2'

def test_get_nonexistent():
    ht = HashTable()
    assert ht.get('nonexistent_key') is None

def test_has():
    ht = HashTable()
    ht.set('key', 'value')
    assert ht.has('key') is True
    assert ht.has('nonexistent_key') is False

def test_keys():
    ht = HashTable()
    ht.set('key1', 'value1')
    ht.set('key2', 'value2')
    ht.set('key3', 'value3')
    assert set(ht.keys()) == {'key1', 'key2', 'key3'}


def test_hash_function():
    ht = HashTable()
    key = 'test_key'
    assert ht.calculate_hash(key) == hash(key) % ht.size


