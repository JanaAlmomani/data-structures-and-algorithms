from .node import Node

class LinkedList:
    """
    A class representing a linked list data structure

    Attributes:
        head: A reference to the first node in the linked list
    
    """
    def __init__(self):
        """
        Initializes a new empty linked list.

        Attributes:
        head: Node or None
            The first node in the linked list, or None if the list is empty.
        
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the linked list in the following format:
        'LinkedList: {value1} -> {value2} -> ... -> {valueN} -> NULL'
        where {value1}, {value2}, ..., {valueN} are the data values of each node in the linked list.
        If the linked list is empty, it returns 'Empty LinkedList'.

        Returns:
            A string representation of the linked list.
        """
        output = ""
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while(current):
                output += f'{{ {current.value} }} -> '
                current = current.next

            output += "NULL"
        return output
    
    def __repr__(self):

        output = ""
        
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output
    
    def to_string(self):
        """
        Returns:
         A string representation of the linked list.
        """
        output = ""
        current_node = self.head
        while current_node:
            output += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next
        output += "NULL"
        return output
    

    
    def insert(self, value):
        """
        Inserts a new node containing the specified value at the **beginning** of the linked list.

        Args:
            value: The value to be stored in the new node.
        """
        node = Node(value)
        node.next = self.head
        self.head = node


    def includes(self,value):
        """
        Searches the linked list for a node containing the specified value.

        Args:
            value: The value to search for in the linked list.

        Returns:
            True if a node with the specified value is found, False otherwise.
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
        
    
    
    def append(self, value):
        """
        Adds a new node containing the specified value to the end of the linked list.

        Args:
            value: The value to be stored in the new node.
        """
        node = Node(value)
        if self.head is None:
         self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node


    def insert_before(self, value, new_value):
        """
        Adds a new node containing the specified new value before the first occurrence of a node with the specified value in the linked list
        
        Args:
            value: The value of the node to insert the new node before.
            new_value: The value to be stored in the new node.
        """
        if not self.head:
            return
        prev_node = None
        current_node = self.head
        while current_node and current_node.value != value:
            prev_node = current_node
            current_node = current_node.next
        if not current_node:
            raise ValueError("Value not found in linked list.")
        new_node = Node(new_value)
        if prev_node:
            prev_node.next = new_node
        else:
            self.head = new_node
        new_node.next = current_node

     
 

    def insert_after(self, value, new_value):
        """
        Adds a new node containing the specified new value after the first occurrence of a node with the specified value in the linked list.
       
        Args:
            value: The value of the node to insert the new node after.
            new_value: The value to be stored
        """
        if self.head is None:
            raise ValueError(f"{value} not found in the list")

        current = self.head
        while current is not None:
            if current.value == value:
                node = Node(new_value)
                node.next = current.next
                current.next = node
                return
            current = current.next

        raise ValueError(f"{value} not found in the list")
        
    
    def kthFromEnd(self, k):
        """
    This method returns the value of the kth node from the end of the linked list.

    Args:
        k (int): The position of the node from the end of the list 

    Returns:
        int or str: The value of the kth node from the end of the list if it exists, 
        or an error message if the list is empty,
        k is larger than the length of the linked list, 
        or k is less than 0.

         """
        #  Edge case 1: k is not a positive integer
        if k < 0:
            raise ValueError("k must be a positive integer")
        
        # Edge case 2: Empty LinkedList
        if self.head is None:
            raise ValueError("List is empty")

        # Edge case 3: k is larger than the length of the linked list
        # if k >= length:
       
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
            
        if k >= length:
            raise ValueError("k is greater than or equal to the length of the list")
        
        # General case
        current_node = self.head
        for _ in range(1, length - k):
            current_node = current_node.next
            
        return current_node.value


  
       
    # def zipLists(list1, list2):
    #     """
    #     Merges two linked lists, alternating nodes between them, and returns a new linked list.

    #     Args:
    #         list1 (LinkedList): The first linked list to merge.
    #         list2 (LinkedList): The second linked list to merge.

    #     Returns:
    #         LinkedList: A new linked list that alternates nodes between list1 and list2, until both are exhausted.
    #             If one of the lists is longer than the other, the remaining nodes are appended to the end of the result.
    #             If both lists are empty, an empty linked list is returned.
    #     """
 
    
def zipLists(list1, list2):
    """
    Merges two linked lists, alternating nodes between them, and returns a new linked list.

    Args:
        list1 (LinkedList): The first linked list to merge.
        list2 (LinkedList): The second linked list to merge.

    Returns:
        LinkedList: A new linked list that alternates nodes between list1 and list2, until both are exhausted.
            If one of the lists is longer than the other, the remaining nodes are appended to the end of the result.
            If both lists are empty, an empty linked list is returned.
    """
    # Handle edge cases where one or both lists are empty
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Initialize pointers to the heads of both lists
    current1 = list1.head
    current2 = list2.head
    
    # Initialize a new linked list
    result = LinkedList()
    last_node = None
    
    # Iterate over both lists simultaneously
    while current1 or current2:
        if current1:
            if not last_node:
                result.head = current1
                last_node = current1
            else:
                last_node.next = current1
                last_node = last_node.next
            current1 = current1.next
            
        if current2:
            if not last_node:
                result.head = current2
                last_node = current2
            else:
                last_node.next = current2
                last_node = last_node.next
            current2 = current2.next
    
    return result






