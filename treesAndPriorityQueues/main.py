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
    triage.add_patient("Diana", 3)
    triage.add_patient("Eli", 1)
    triage.add_patient("Tom", 4)
    triage.add_patient("Alice", 5)
    triage.add_patient("Rachel", 4)

    next_patient = triage.peek_next()
    print("Next patient:", next_patient[0], "(Severity", next_patient[1], ")")

    print()
    print("Processing patients:")

    while not triage.is_empty():
        name, severity = triage.process_next()
        print("Now treating:", name, "(Severity", severity, ")")

    print()


def main():
    test_part1()
    test_part3()


if __name__ == "__main__":
    main()