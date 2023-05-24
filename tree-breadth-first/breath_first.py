class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first(tree):
    """Performs breadth-first traversal on a binary tree.

    Args:
        tree (Node): The root node of the binary tree.

    Returns:
        list: A list containing the values of the nodes visited in breadth-first order.

    Raises:
        None

    """
    if tree is None:
        return "Empty tree"

    result = []
    queue = [tree]  # Use list initialization instead of append

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


# Create the nodes and build the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Call the breadth_first function
result = breadth_first(root)

# Print the result
print(result)  #[1, 2, 3, 4, 5, 6, 7]