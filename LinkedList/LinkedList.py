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
        where {value1}, {value2}, ..., {valueN} are the data values of each node in the linked list
        If the linked list is empty, it returns 'Empty LinkedList'

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
         A string representation of the linked list
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
        Inserts a new node containing the specified value at the **beginning** of the linked list

        Args:
            value: The value to be stored in the new node.
        """
        node = Node(value)
        node.next = self.head
        self.head = node


    def includes(self,value):
        """
        Searches the linked list for a node containing the specified value

        Args:
            value: The value to search for in the linked list

        Returns:
            True if a node with the specified value is found, False otherwise
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
        
    
    
