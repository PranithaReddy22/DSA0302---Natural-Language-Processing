

words = ["connected", "connecting", "connection"]


base_form = "connect"


rules = {
    "ed": ("Inflectional", "Past Tense"),
    "ing": ("Inflectional", "Present Participle"),
    "ion": ("Derivational", "Noun Formation")
}

print("=" * 90)
print("{:<15} {:<15} {:<12} {:<18} {:<15} {:<15}".format(
    "Word", "Root", "Suffix", "Suffix Type", "Parsed Structure", "Normalized"))
print("=" * 90)

for word in words:

    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        suffix_type = rules["ed"][0]

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        suffix_type = rules["ing"][0]

    elif word.endswith("ion"):
       
        root = "connect"
        suffix = "ion"
        suffix_type = rules["ion"][0]

    else:
        root = word
        suffix = "-"
        suffix_type = "-"

    parsed = root + " + " + suffix

    print("{:<15} {:<15} {:<12} {:<18} {:<15} {:<15}".format(
        word, root, suffix, suffix_type, parsed, base_form))