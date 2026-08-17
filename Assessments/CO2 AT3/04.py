from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "watches",
    "watching",
    "washable",
    "washer",
    "washed"
]

print("Word -> Stem")
print("------------")

for word in words:
    print(word, "->", ps.stem(word))