# Challenge Title: Linked List Implementation(Extending an Implementation)
## Code Challenge: Class 06 
## Feature Tasks
Write the following methods for the Linked List class:
- append
- insert before
- insert after

## Whiteboard Process
![]()
## Approach & Efficiency
## Algorithm :
- The algorithm for the append function in a singly linked list is:

1. Create a new node with the given value
2. If the linked list is empty, set the new node as the head of the list and return
3. Traverse the linked list to find the last node
4. Set the next pointer of the last node to point to the new node

- The algorithm for the insert_before function in a singly linked list is:

1. If the linked list is empty (the head node is None), then print message and return.
2. If the value to be inserted before is the value of the head node, call the **insert method(First)**to insert the new node at the beginning of the list and return.
3. Traverse the linked list starting from the second node (the node after the head node) until either the end of the list is reached or the node before which the new node will be inserted is found.
4. If the node before which the new node will be inserted is found, create a new node with the given new value and set its next pointer to point to the current node. Then, set the next pointer of the previous node to point to the new node.
5. If the end of the list is reached without finding the node before which the new node will be inserted, print message 

- The algorithm for the insert_after function in a singly linked list is:
1. Check if the list is empty by checking if the head is None. If it is, print a message that the value cannot be found in the list and return
2. Set the current node to the head of the list
3. Traverse the list using a loop, checking if the current node's value is equal to the value to be inserted after
4. If the value is found, **create a new node with the value** to be inserted after and set its next pointer to the current node's next pointer
5. Set the current node's next pointer to the new node
6. Return the updated linked list

**If the value is not found, the loop will terminate and a message will be printed indicating that the value could not be found in the list**



## Big O :
- **For the first method :append** 
The time complexity is  O(n) : where n is the number of nodes in the list, we need to traverse the list from the beginning to the end to find the last node and then added the new node

The space complexity is  O(1) : which means that the amount of memory space needed is constant and does not depend on the size of the input, because the function does not create any new data structures that take up extra memory. Instead, it is modify the existing linked list by adding new nodes or changing the links between nodes

- **For the second method :insert before** 
The time complexity is  O(n) : where n is the number of nodes in the list , it requires traversing the entire list to find the node before which the new node will be inserted

The space complexity is O(1) : which means that the amount of memory space needed is constant and does not depend on the size of the input, because the function does not create any new data structures that take up extra memory. Instead, it is modify the existing linked list by adding new nodes or changing the links between nodes


- **For the thared method :insert after** 
The time complexity is  O(n) : where n is the number of nodes in the list , it requires traversing the entire list to find the node after which the new node will be inserted

The space complexity is O(1) : which means that the amount of memory space needed is constant and does not depend on the size of the input, because the function does not create any new data structures that take up extra memory. Instead, it is modify the existing linked list by adding new nodes or changing the links between nodes



## Solution
### [click here to go to the code](./LinkedList/LinkedList.py)
### [click here to go to the test code](./tests/test_ll.py)


To run the code:
-on your terminal follow these command:
1. source .venv/bin/activate
2. pip install pytest
3. pytest
