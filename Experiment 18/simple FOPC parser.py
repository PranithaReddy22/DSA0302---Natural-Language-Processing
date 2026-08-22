import re

def parse_fopc(expression):
    expression = expression.strip()

    # Check for logical operators
    operators = {
        "AND": "∧",
        "OR": "∨",
        "NOT": "¬",
        "IMPLIES": "→"
    }

    print("\nExpression:", expression)

    found = False

    for word, symbol in operators.items():
        if word in expression.upper():
            print("Logical Operator:", word, "(" + symbol + ")")
            found = True

    # Find predicates such as Student(Ravi)
    predicates = re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\s*\([^)]*\)', expression)

    if predicates:
        print("Predicates:")
        for predicate in predicates:
            print(" ", predicate)
    else:
        print("No predicates found.")

    # Find variables/constants
    terms = re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', expression)

    print("Terms:", terms)

    if found or predicates:
        print("Valid basic FOPC expression.")
    else:
        print("Expression could not be parsed.")


expression = input("Enter a basic FOPC expression: ")

parse_fopc(expression)