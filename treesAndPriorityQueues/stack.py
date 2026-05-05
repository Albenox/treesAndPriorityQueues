# stack.py
# This file contains a simple Stack class


class Stack:
    def __init__(self):
        # List used to store stack items
        self.items = []

    def is_empty(self):
        # Returns True if the stack has no items
        return len(self.items) == 0

    def push(self, item):
        # Adds an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Removes and returns the top item
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        return self.items.pop()

    def top(self):
        # Returns the top item without removing it
        if self.is_empty():
            raise IndexError("Cannot view the top of an empty stack.")

        return self.items[-1]

    def size(self):
        # Returns how many items are in the stack
        return len(self.items)

    def build_from_postfix(self, postfix):
        # Clears any existing tree
        self.clear_tree()

        stack = Stack()
        tokens = postfix.split()

        for token in tokens:
            # For now, assume everything is a number
            node = TreeNode(token)
            stack.push(node)

        # Set the last item as the root
        if stack.size() > 0:
            self.root = stack.pop()