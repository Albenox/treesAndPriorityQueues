# main.py
# This program tests classes

from binary_expression_tree import BinaryExpressionTree
from triage_system import TriageSystem


def test_part1():
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


def test_part3():
    print("----- Hospital Triage System -----")

    triage = TriageSystem()

    triage.add_patient("Sofia", 5)
    triage.add_patient("Bob", 2)
    triage.add_patient("Charlie", 4)

    print("Queue empty?", triage.is_empty())
    print("Queue size:", triage.size())

    triage.clear()
    print("Queue cleared.")
    print("Queue size after clear:", triage.size())
    print()


def main():
    test_part1()
    test_part3()


if __name__ == "__main__":
    main()