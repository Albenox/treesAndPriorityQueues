# main.py
# This program tests the starting framework and Stack class

from binary_expression_tree import BinaryExpressionTree
from stack import Stack


def main():
    print("----- Binary Expression Tree Part-----")

    tree = BinaryExpressionTree()

    expression = "5 3 8"

    tree.build_from_postfix(expression)

    print("Postfix:", expression)

    if not tree.is_empty():
        print("Root value:", tree.root.value)
    else:
        print("Tree is empty")


if __name__ == "__main__":
    main()