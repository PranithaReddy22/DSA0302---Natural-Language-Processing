# Morphological Parser

words = ["disagree", "agreement", "agreeable"]

print("{:<15}{:<10}{:<10}{:<12}{:<15}{:<25}{:<12}".format(
    "Original", "Prefix", "Root", "Suffix",
    "Category", "Meaning", "Normalized"))

for word in words:

    if word == "disagree":
        prefix = "dis-"
        root = "agree"
        suffix = "-"
        category = "Derivational"
        meaning = "Opposite of agree"
        normalized = "agree"

    elif word == "agreement":
        prefix = "-"
        root = "agree"
        suffix = "-ment"
        category = "Derivational"
        meaning = "State of agreeing"
        normalized = "agree"

    elif word == "agreeable":
        prefix = "-"
        root = "agree"
        suffix = "-able"
        category = "Derivational"
        meaning = "Able to agree/Pleasant"
        normalized = "agree"

    print("{:<15}{:<10}{:<10}{:<12}{:<15}{:<25}{:<12}".format(
        word, prefix, root, suffix,
        category, meaning, normalized))