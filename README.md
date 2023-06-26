# Challenge Title: Hash Tables
## Implement a Hashtable Class with the following methods: set,get,has,keys,hash

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency

- set(self, key, value)

    Time Complexity:

    - Best Case: O(1) when there are no collisions.

    - Worst Case: O(n) when there are many collisions and the linear search is required.
    
    Space Complexity: O(1)

- def get(self, key)

    Time Complexity:

    - Best Case: O(1) when the key is found at the first position in its bucket.

    - Worst Case: O(n) when the key is the last one in its bucket or it doesn't exist.

    Space Complexity: O(1)

- def has(self, key)

    Time Complexity:

    - Best Case: O(1) when the key is found at the first position in its bucket.

    - Worst Case: O(n) when the key is the last one in its bucket or it doesn't exist.
    
    Space Complexity: O(1)

 def keys(self)

    Time Complexity: O(n), where n is the total number of entries in the hashtable.
    
    Space Complexity: O(n), as the returned list holds all the keys.

def hash(self, key)

    Time Complexity: O(1)
    
    Space Complexity: O(1)

## Solution
[The Code Link](./hashtable/hashtable/hashtable.py)
[The Test Code Link](./hashtable/tests/hashtable_test.py)

- To run the code :

    python3 -m venv .venv

    source .venv/bin/activate
    
- To run the Test:

    pytest

