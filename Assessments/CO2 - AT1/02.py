

words = ["unhappy", "happiness", "happily"]

print("=" * 95)
print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<20} {:<10}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Breakdown", "Normalized"))
print("=" * 95)

for word in words:
    prefix = "-"
    suffix = "-"
    root = "happy"
    mtype = "Derivational"

    if word == "unhappy":
        prefix = "un"
    elif word == "happiness":
        suffix = "ness"
    elif word == "happily":
        suffix = "ly"

    breakdown = f"{prefix} + {root}" if prefix != "-" else f"{root} + {suffix}"

    print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<20} {:<10}".format(
        word, prefix, root, suffix, mtype, breakdown, root))