class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order_traversal(self, node, result):
        if node:
            result.append(node.value)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    def in_order_traversal(self, node, result):
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)
        return result

    def post_order_traversal(self, node, result):
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.value)
        return result
    
    def find_maximum_value(self):
        if self.root is None:
            raise ValueError("The tree is empty.")

        return self._find_maximum_value_recursive(self.root)

    def _find_maximum_value_recursive(self, node):
        if node is None:
            return float('-inf')

        max_value = node.value
        left_max = self._find_maximum_value_recursive(node.left)
        right_max = self._find_maximum_value_recursive(node.right)

        if left_max > max_value:
            max_value = left_max
        if right_max > max_value:
            max_value = right_max

        return max_value
    
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()


    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)

tree = BinaryTree()
tree.root = Node("A")
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")
tree.root.right.left = Node("F")
tree.root.right.right = Node("G")

pre_order_result = tree.pre_order_traversal(tree.root, [])
print("Pre-order", pre_order_result)

in_order_result = tree.in_order_traversal(tree.root, [])
print("In-order", in_order_result)

post_order_result = tree.post_order_traversal(tree.root, [])
print("Post-order", post_order_result)


# Binary Search Tree testing
bst = BinarySearchTree()
bst.add(4)
bst.add(2)
bst.add(6)
bst.add(1)
bst.add(3)
bst.add(5)
bst.add(7)

print("Contains 2:", bst.contains(2))  # True
print("Contains 8:", bst.contains(8))  # False

tree1 = BinaryTree()
tree1.root = Node(1)
tree1.root.left = Node(6)
tree1.root.right = Node(8)
tree1.root.left.left = Node(9)
tree1.root.left.right = Node(11)
tree1.root.right.left = Node(2)
tree1.root.right.right = Node(5)

max_value = tree1.find_maximum_value()
print("Maximum value:", max_value)  # Output: Maximum value: 11