prefixes = ["un", "re"]
suffixes = ["est", "able", "ing", "s"]

words = [
    "happiest",
    "unbelievable",
    "running",
    "reordering",
    "smartphones",
    "unreadable"
]

# Original simple parser
def old_parser(word):
    for suffix in suffixes:
        if word.endswith(suffix):
            root = word[:-len(suffix)]
            return root, suffix

    return word, "None"


print("BEFORE CORRECTION")
print("------------------")

for word in words:
    print(word, "->", old_parser(word))


# Improved parser
def new_parser(word):

    original = word
    found_prefix = ""
    found_suffix = ""

    # Check prefix
    for prefix in prefixes:
        if word.startswith(prefix):
            found_prefix = prefix
            word = word[len(prefix):]
            break

    # Check suffix
    for suffix in sorted(suffixes, key=len, reverse=True):
        if word.endswith(suffix):
            found_suffix = suffix
            word = word[:-len(suffix)]
            break

    return original, found_prefix, word, found_suffix


print("\nAFTER CORRECTION")
print("----------------")

for word in words:
    print(new_parser(word))