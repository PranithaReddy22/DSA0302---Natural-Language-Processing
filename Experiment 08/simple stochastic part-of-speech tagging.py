
pos_prob = {
    "i": "PRP",
    "am": "VBP",
    "a": "DT",
    "student": "NN",
    "love": "VBP",
    "python": "NNP",
    "natural": "JJ",
    "language": "NN",
    "processing": "NN",
    "is": "VBZ",
    "interesting": "JJ"
}


sentence = input("Enter a sentence: ").lower()


words = sentence.split()


print("\nPOS Tags:")
for word in words:
    tag = pos_prob.get(word, "NN")   
    print(word, "->", tag)