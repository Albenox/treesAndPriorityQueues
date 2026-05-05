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

    def build_from_postfix(self, postfix):
        # Clears any existing tree
        self.clear_tree()

        stack = Stack()
        tokens = postfix.split()
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            # If the token is a number, create a tree node
            if self._is_number(token):
                node = TreeNode(token)
                stack.push(node)

            # If the token is an operator, connect two previous nodes
            elif token in operators:
                operator_node = TreeNode(token)

                # Right side is popped first
                operator_node.right = stack.pop()

                # Left side is popped second
                operator_node.left = stack.pop()

                # Push the new mini-tree back onto the stack
                stack.push(operator_node)

            else:
                raise ValueError(f"Unsupported token: {token}")

        # The final item left is the full expression tree
        if stack.size() > 0:
            self.root = stack.pop()
    
    def _is_number(self, token):
        # Checks if the token can be converted into a number
        try:
            float(token)
            return True
        except ValueError:
            return False