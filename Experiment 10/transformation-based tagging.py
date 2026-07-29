
sentence = input("Enter a sentence: ").lower()


words = sentence.split()


tags = ["NN"] * len(words)

#
for i, word in enumerate(words):
    if word in ["is", "am", "are", "was", "were"]:
        tags[i] = "VB"
    elif word.endswith("ing"):
        tags[i] = "VBG"
    elif word.endswith("ed"):
        tags[i] = "VBD"
    elif word.endswith("ly"):
        tags[i] = "RB"
    elif word in ["a", "an", "the"]:
        tags[i] = "DT"


print("\nPOS Tags:")
for word, tag in zip(words, tags):
    print(word, "->", tag)