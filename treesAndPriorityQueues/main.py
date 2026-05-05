# main.py
# This program tests the starting framework for BinaryExpressionTree

from binary_expression_tree import BinaryExpressionTree


def main():
    tree = BinaryExpressionTree()

    print("----- Binary Expression Tree Part 1A-1 -----")
    print("Tree empty?", tree.is_empty())

    tree.clear_tree()
    print("Tree cleared.")


if __name__ == "__main__":
    main()