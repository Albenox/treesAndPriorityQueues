# binary_expression_tree.py
# This file will contain the BinaryExpressionTree class

from stack import Stack

class TreeNode:
    def __init__(self, value):
        # Stores either a number or an operator
        self.value = value

        # Left and right child nodes
        self.left = None
        self.right = None


class BinaryExpressionTree:
    def __init__(self):
        # Root starts as None because the tree is empty
        self.root = None

    def is_empty(self):
        # Returns True if the tree has no nodes
        return self.root is None

    def clear_tree(self):
        # Clears the tree by removing the root
        self.root = None