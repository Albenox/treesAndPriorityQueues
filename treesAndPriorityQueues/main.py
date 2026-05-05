# main.py
# This program tests the starting framework and Stack class

from binary_expression_tree import BinaryExpressionTree
from stack import Stack


def main():
    tree = BinaryExpressionTree()

    print("----- Binary Expression Tree Part 1A-2 -----")
    print("Tree empty?", tree.is_empty())

    stack = Stack()
    print("Stack empty?", stack.is_empty())

    stack.push("5")
    stack.push("3")

    print("Stack size after pushes:", stack.size())
    print("Top item:", stack.top())
    print("Popped item:", stack.pop())
    print("Stack size after pop:", stack.size())


if __name__ == "__main__":
    main()