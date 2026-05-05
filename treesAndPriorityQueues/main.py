# main.py
# This program tests the BinaryExpressionTree class

from binary_expression_tree import BinaryExpressionTree


def main():
    print("----- Binary Expression Tree -----")

    expressions = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +"
    ]

    for expression in expressions:
        tree = BinaryExpressionTree()
        tree.build_from_postfix(expression)

        print("Postfix Expression:", expression)
        print("Infix Expression:  ", tree.infix_traversal())
        print("Postfix Output:    ", tree.postfix_traversal())
        print("Evaluated Result:  ", tree.evaluate_tree())
        print()


if __name__ == "__main__":
    main()