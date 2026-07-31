

words = ["writes", "writing", "written"]

print("Finite-State Morphological Parsing")
print("-" * 80)

for word in words:

    if word == "writes":
        root = "write"
        breakdown = "write + -s"
        transition = "Start -> Root(write) -> Suffix(-s) -> Final"
        classification = "Regular Inflection"

    elif word == "writing":
        root = "write"
        breakdown = "write + -ing"
        transition = "Start -> Root(write) -> Suffix(-ing) -> Final"
        classification = "Regular Inflection"

    elif word == "written":
        root = "write"
        breakdown = "write + irregular form"
        transition = "Start -> Root(write) -> Irregular(written) -> Final"
        classification = "Irregular Inflection"

    print("\nOriginal Word :", word)
    print("State Path    :", transition)
    print("Breakdown     :", breakdown)
    print("Root Form     :", root)
    print("Classification:", classification)
    print("Normalized    :", root)