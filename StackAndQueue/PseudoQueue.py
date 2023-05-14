from .stack import Stack

class PseudoQueue:

    def __init__(self):
        """
        Initializes an empty PseudoQueue.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """
        Adds a new node with the given value to the back of the PseudoQueue.

        First, push the new value onto stack2.
        Then, pop all elements from stack2 and push them onto stack1.
        This effectively reverses the order of the elements in stack2,
        making the new value the last element in the queue.
        """
        self.stack2.push(value)
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        """
        Removes and returns the value of the front node of the PseudoQueue.
        """
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise IndexError("PseudoQueue is empty. Cannot perform dequeue operation")
        
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        value = self.stack2.pop()

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

        return value

    def is_empty(self):
        """
        Check if the PseudoQueue is empty or not

        Returns:
            True if the PseudoQueue is empty.
            False otherwise.
        """
        return self.stack1.is_empty() and self.stack2.is_empty()
    
    def __str__(self):
        """
        Returns a string representation of the PseudoQueue.

        If the PseudoQueue is empty, returns "Empty PseudoQueue".
        Otherwise, returns the string representation of the queue.
        """
        if self.stack1.is_empty():
            return "Empty PseudoQueue"

        result = "None <-- "
        current_node = self.stack1.top
        while current_node is not None:
            result += str(current_node.value) + " <-- "
            current_node = current_node.next

        return result[:-5]


    
    
# ll=PseudoQueue()
# ll.enqueue(1)
# ll.enqueue(2)
# ll.enqueue(3)
# print(ll.dequeue())
# ll.enqueue(4)
# print(ll.dequeue())

