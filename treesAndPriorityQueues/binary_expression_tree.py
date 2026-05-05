# binary_expression_tree.py
# This file contains the BinaryExpressionTree class

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

            # If the token is an operator, connect nodes
            elif token in operators:
                operator_node = TreeNode(token)

                # Pop right then left
                operator_node.right = stack.pop()
                operator_node.left = stack.pop()

                # Push the new subtree back
                stack.push(operator_node)

            else:
                raise ValueError(f"Unsupported token: {token}")

        # Final tree root
        if stack.size() != 1:
            raise ValueError("Invalid postfix expression.")

        self.root = stack.pop()

    def infix_traversal(self):
        if self.is_empty():
            raise ValueError("Cannot traverse an empty tree.")

        return self._inorder(self.root)

    def _inorder(self, node):
        # Leaf node (number)
        if node.left is None and node.right is None:
            return node.value

        # Left, root, right
        return f"({self._inorder(node.left)} {node.value} {self._inorder(node.right)} )"

    def postfix_traversal(self):
        if self.is_empty():
            raise ValueError("Cannot traverse an empty tree.")

        return self._postorder(self.root)

    def _postorder(self, node):
        # Leaf node (number)
        if node.left is None and node.right is None:
            return node.value

        # Left, right, root
        return f"{self._postorder(node.left)} {self._postorder(node.right)} {node.value}"

    def evaluate_tree(self):
        if self.is_empty():
            raise ValueError("Cannot evaluate an empty tree.")

        return self._evaluate(self.root)

    def _evaluate(self, node):
        # Leaf node (number)
        if node.left is None and node.right is None:
            return float(node.value)

        # Recursively evaluate
        left_val = self._evaluate(node.left)
        right_val = self._evaluate(node.right)

        if node.value == "+":
            return left_val + right_val
        elif node.value == "-":
            return left_val - right_val
        elif node.value == "*":
            return left_val * right_val
        elif node.value == "/":
            if right_val == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return left_val / right_val

    def _is_number(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False