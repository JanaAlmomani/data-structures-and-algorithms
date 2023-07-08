from tree_intersection.tree_intersection.tree_intersection import *
import pytest 

def test_tree_intersection1():
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

    # Asserting the common values
    assert result == {1, 2, 3, 4, 5, 7}

def test_tree_intersection2():
    # Binary Tree 1
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)


    # Binary Tree 2
    tree2 = TreeNode(3)
    tree2.left = TreeNode(4)
    tree2.right = TreeNode(7)
    tree2.left.left = TreeNode(9)

    # Calling tree_intersection function
    result = tree_intersection(tree1, tree2)

    # Asserting the common values
    assert result == {3, 4}


def test_tree_intersection3():
    # Binary Tree 1
    tree1 = TreeNode(None)

    # Binary Tree 2
    tree2 = TreeNode(3)

    # Calling tree_intersection function
    result = tree_intersection(tree1, tree2)

    # Asserting the common values
    assert result == set()