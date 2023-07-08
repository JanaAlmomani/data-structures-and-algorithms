class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [None] * self.size

    #     def hash(self, key):
    #         return hash(key) % self.size



    def calculate_hash(self, key):  # In the test cases i faced a recursion error in the code because
                                    # the hash method calls itself instead of using the built-in hash function ,
                                    # To fix this, i  need to change the name of the hash method to something different 
        return hash(key) % self.size

    def set(self, key, value):
        index = self.calculate_hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Replace value if key already exists
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.calculate_hash(key)
        if self.table[index] is None:
            return None
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def has(self, key):
        index = self.calculate_hash(key)
        if self.table[index] is None:
            return False
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self.table:
            if bucket is not None:
                for pair in bucket:
                    keys.append(pair[0])
        return keys

    def calculate_hash(self, key):
        return hash(key) % self.size



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
