from LinkedList.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

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
    
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
        
    def __str__(self):
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
    
    def append(self, value):
        """
        This method inorder to adds a new node with a specified value to the end of the list
        
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
        if self.head is None:
            print(f"{value} not found in the list")
            return

        if self.head.value == value:
            self.insert_first(new_value)
            return

        current = self.head.next
        prev = self.head

        while current is not None:
            if current.value == value:
                node = Node(new_value)
                node.next = current
                prev.next = node
                return
            prev = current
            current = current.next

        print(f"{value} not found in the list")

    def insert_after(self, value, new_value):
        if self.head is None:
            print(f"{value} not found in the list")
            return

        current = self.head
        while current is not None:
            if current.value == value:
                node = Node(new_value)
                node.next = current.next
                current.next = node
                return
            current = current.next

        print(f"{value} not found in the list")

        

ll = LinkedList()

ll.insert(3)
ll.insert(5)
ll.insert(2)
ll.insert(1)
ll.insert(6)
ll.insert(9)

# print(ll.includes(9))
ll.append(0)
ll.insert(10)
ll.append(20)
ll.insert_before(0,1)
# ll.insert_before(7,1)
ll.insert_after(7,1)
ll.insert_after(20,30)
ll.append(20)
print(ll)  # "1 -> 2 -> 3 -> None"
# print(ll.includes(2))  # True
# print(ll.includes(4))  # False

# print(ll)