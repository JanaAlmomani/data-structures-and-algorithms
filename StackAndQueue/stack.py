class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:

    """
    A class representing a stack data structure
    """
    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        """
        Returns a string representation of the Stack

        Returns:
            A string representing the Stack in this format value --> value --> value ........ --> None
        """
        output = ""
        if self.top is None:
            output = "Empty Stack"
        else:
            current = self.top
            while(current):
                output += f'{current.value} --> '
                current = current.next
            output += " None"
        return output
    
    def __repr__(self):
        """
        Returns a string representation of the stack, similar to __str__()

        Returns:
            A string representing the stack
        """
        output = ""
        if self.top is None:
            output = "Empty Stack"
        else:
            current = self.top
            while(current):
                output += f'{current.value} --> '
                current = current.next
            output += " None"
        return output   
    def push(self,value):
        """
        Adds a new Node with the given value to the top of the stack

        Args: 
            value -> Any value to be added to the top of the stack

        Returns:
            None
        """
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        """
        Removes and returns the top element from the stack

        Returns:
          The value from node from the top of the stack

        Raises:
            raises Exception -> If the stack is empty
        """
        if self.top is not None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
             raise Exception ("Stack is empty")

    def peek(self):
        """
        Returns the value of the top element from the stack without removing it

        Returns:
          The Value of the node located at the top of the stack

        Raises:
            raises Exception -> If the stack is empty
        """
        if self.top:
            return self.top.value
        else:
            raise Exception("This stack is empty")
   
    def is_empty(self):
        """
        Returns True if the stack is empty, otherwise False

        Returns: 
            True if the stack is empty, False otherwise
        """
        return self.size == 0
