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
    
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()


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
