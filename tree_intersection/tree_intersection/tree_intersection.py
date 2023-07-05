from hashtable.hashtable.hashtable import HashTable

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_intersection(tree1, tree2):
    values_set = set()
    hash_table = HashTable()

    def traverse_tree(node):
        if node is None:
            return
        hash_table.set(node.value, True)
        traverse_tree(node.left)
        traverse_tree(node.right)

    traverse_tree(tree1)
    
    def find_common_values(node):
        if node is None:
            return
        if hash_table.has(node.value):
            values_set.add(node.value)
        find_common_values(node.left)
        find_common_values(node.right)

    find_common_values(tree2)
    
    return values_set


# Binary Tree 1
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)
tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(7)

# Binary Tree 2
tree2 = TreeNode(3)
tree2.left = TreeNode(4)
tree2.right = TreeNode(7)
tree2.left.left = TreeNode(9)
tree2.left.right = TreeNode(5)
tree2.right.left = TreeNode(1)
tree2.right.right = TreeNode(2)

# Calling tree_intersection function
result = tree_intersection(tree1, tree2)

# Printing the common values
print(result)
