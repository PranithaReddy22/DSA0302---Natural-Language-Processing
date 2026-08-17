import re
from nltk.stem import PorterStemmer

ps = PorterStemmer()

text = """
infection infectious infected infect
infections infecting
inflammatory inflammation
treatment treatments treated treating
patient patients
"""

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

print("Original Word -> Porter Stem")
print("--------------------------------")

for word in words:
    print(word, "->", ps.stem(word))

print("\nImportant biomedical examples:")

test_words = [
    "infection",
    "infectious",
    "infected",
    "infect",
    "inflammation",
    "inflammatory"
]

for word in test_words:
    print(word, "->", ps.stem(word))