# Q6 - Morphological Parser for Plural Nouns

# Irregular plural dictionary
irregular = {
    "children": "child",
    "men": "man",
    "women": "woman",
    "mice": "mouse",
    "feet": "foot",
    "teeth": "tooth",
    "geese": "goose"
}


def parser(word):

    # Irregular plurals
    if word in irregular:
        return irregular[word], "Plural Noun"

    # Plurals ending in -ies
    if word.endswith("ies"):
        return word[:-3] + "y", "Plural Noun"

    # Plurals ending in -es
    if word.endswith("es"):
        return word[:-2], "Plural Noun"

    # Regular plurals ending in -s
    if word.endswith("s"):
        return word[:-1], "Plural Noun"

    # Singular
    return word, "Singular"


# Test words
words = [
    "car",
    "cars",
    "box",
    "boxes",
    "city",
    "cities",
    "dog",
    "dogs",
    "child",
    "children",
    "mouse",
    "mice"
]


print("WORD -> ANALYSIS")
print("----------------")

for word in words:
    print(word, "->", parser(word))