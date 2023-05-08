from .stack import Stack

class PseudoQueue:

    def __init__(self):
        """
        Initializes an empty PseudoQueue.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self):
        """
        Returns a string representation of the PseudoQueue.

        If the PseudoQueue is empty, returns "Empty PseudoQueue".
        Otherwise, returns the string representation of stack1.
        """
        if self.stack1.is_empty():
            return "Empty PseudoQueue"
        return str(self.stack1)

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

        If the PseudoQueue is empty, raises an IndexError.
        Otherwise, pop all elements from stack1 and push them onto stack2 in reverse order.
        Then, pop the top element from stack2 (which is the front element of the PseudoQueue),
        and reverse the order of the elements in stack2 again by popping them all off
        stack2 and pushing them back onto stack1.
        Finally, return the popped value.
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