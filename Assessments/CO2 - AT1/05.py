

words = ["relational", "relation", "relate"]

print("Porter Stemmer Analysis")
print("-" * 70)

for word in words:

    if word == "relational":
        rule = "Remove -ational -> relate, then remove -e"
        intermediate = "relate"
        stem = "relat"

    elif word == "relation":
        rule = "Remove -ion"
        intermediate = "relat"
        stem = "relat"

    elif word == "relate":
        rule = "Remove -e"
        intermediate = "relat"
        stem = "relat"

    print(f"\nOriginal Word : {word}")
    print(f"Applied Rule  : {rule}")
    print(f"Intermediate  : {intermediate}")
    print(f"Final Stem    : {stem}")