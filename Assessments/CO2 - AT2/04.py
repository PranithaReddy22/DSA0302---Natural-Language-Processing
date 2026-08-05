# Morphological Parsing and Normalization

words = ["activate", "activation", "reactivation"]

print("{:<15}{:<10}{:<10}{:<12}{:<25}{:<15}{:<20}".format(
    "Original", "Prefix", "Root", "Suffix",
    "Sequence", "Normalized", "Parsed"))

for word in words:

    if word == "activate":
        prefix = "-"
        root = "active"
        suffix = "-ate"
        sequence = "active + ate"
        normalized = "active"

    elif word == "activation":
        prefix = "-"
        root = "active"
        suffix = "-ation"
        sequence = "active + ate + ion"
        normalized = "active"

    elif word == "reactivation":
        prefix = "re-"
        root = "active"
        suffix = "-ation"
        sequence = "re + active + ate + ion"
        normalized = "active"

    parsed = prefix + " " + root + " " + suffix

    print("{:<15}{:<10}{:<10}{:<12}{:<25}{:<15}{:<20}".format(
        word, prefix, root, suffix,
        sequence, normalized, parsed))