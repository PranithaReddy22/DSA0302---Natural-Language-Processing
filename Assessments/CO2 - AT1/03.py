

words = ["played", "player", "playing"]

print("Morphological Analysis")
print("-" * 75)

for word in words:
    if word.endswith("ed"):
        stem = word[:-2]
        affix = "-ed"
        ttype = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "-ing"
        ttype = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "-er"
        ttype = "Derivational"

    else:
        stem = word
        affix = "-"
        ttype = "None"

    print(f"\nOriginal Word      : {word}")
    print(f"Extracted Stem     : {stem}")
    print(f"Removed Affix      : {affix}")
    print(f"Transformation     : {ttype}")
    print(f"Normalized Form    : {stem}")