class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    """
    A class representing a Queue data structure
    """
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __str__(self):
        """
        Returns a string representation of the queue

        Returns:
            A string representing the queue in this format value --> value --> value ........ --> None
        """
        output = ""
        if self.front is None:
            output = "Empty Queue"
        else:
            current = self.front
            while current:
                output += f"{current.value} --> "
                current = current.next
            output += "None"
        return output

    def __repr__(self):
        """
        Returns a string representation of the queue, similar to __str__()

        Returns:
            A string representing the queue.
        """
        output = ""
        if self.front is None:
            output = "Empty Queue"
        else:
            current = self.front
            while current:
                output += f"{current.value} --> "
                current = current.next
            output += "None"
        return output

    def enqueue(self,value):
        """Adds a new node with the given value to the rear of the queue

        Args:
            value: the value of the node to be added

        Returns:
            None
        """
        node = Node(value)

        #if the queue is empty
        if not self.rear:
            self.front = node
            self.rear = node
           
        else:
            self.rear.next = node
            self.rear = node

        self.size += 1

    def dequeue(self):
        """Removes and returns the node at the front of the queue

        Raises:
            Exception: If the queue is empty

        Returns:
            The value of the node that was removed
        """
        #if the queue is empty
        if self.front == None:
            raise Exception("Cannot dequeue from an empty queue")
        # if the queue contains only one node
        if self.front == self.rear:
            self.rear = None
            #self.front = None
        temp = self.front
        self.front = self.front.next
        temp.next = None
        self.size -= 1

        return temp.value

    def peek(self):
        """Returns the value of the node at the front of the queue without removing it

        Raises:
            Exception: If the queue is empty

        Returns:
            The value of the node at the front of the queue
        """
        if self.front == None:
            raise Exception("This queue is empty")  
        return self.front.value
        
    
    def is_empty(self):
        """
        Returns True if the queue is empty, otherwise False

        Returns:
            True if the queue is empty, otherwise False
        """
       
        return self.size == 0