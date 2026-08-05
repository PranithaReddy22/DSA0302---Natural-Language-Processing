# Morphology-Based Normalization

words = ["govern", "government", "governance"]

print("{:<15}{:<10}{:<15}{:<20}{:<15}{:<15}".format(
    "Original", "Root", "Affix", "Hierarchy",
    "Normalized", "Final Output"))

for word in words:

    if word == "govern":
        root = "govern"
        affix = "-"
        hierarchy = "Level 0"
        normalized = "govern"

    elif word == "government":
        root = "govern"
        affix = "-ment"
        hierarchy = "Level 1"
        normalized = "govern"

    elif word == "governance":
        root = "govern"
        affix = "-ance"
        hierarchy = "Level 1"
        normalized = "govern"

    print("{:<15}{:<10}{:<15}{:<20}{:<15}{:<15}".format(
        word, root, affix,
        hierarchy, normalized, normalized))