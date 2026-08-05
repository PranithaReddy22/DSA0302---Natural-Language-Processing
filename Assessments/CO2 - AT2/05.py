# Inflectional Morphology Normalization

words = ["create", "creates", "creating"]

print("{:<15}{:<12}{:<25}{:<12}{:<15}{:<15}".format(
    "Original", "Suffix", "Grammar",
    "Root", "Normalized", "Output"))

for word in words:

    if word == "create":
        suffix = "-"
        grammar = "Base Form"
        root = "create"
        normalized = "create"

    elif word == "creates":
        suffix = "-s"
        grammar = "Third Person Singular"
        root = "create"
        normalized = "create"

    elif word == "creating":
        suffix = "-ing"
        grammar = "Present Participle"
        root = "create"
        normalized = "create"

    print("{:<15}{:<12}{:<25}{:<12}{:<15}{:<15}".format(
        word, suffix, grammar,
        root, normalized, normalized))