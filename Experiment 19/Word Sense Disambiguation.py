import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Download required resources once
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('punkt_tab')

sentence = input("Enter a sentence: ")
word = input("Enter the ambiguous word: ")

tokens = word_tokenize(sentence)

sense = lesk(tokens, word)

print("\nSentence:", sentence)
print("Word:", word)

if sense:
    print("Best Sense:", sense.name())
    print("Definition:", sense.definition())
    print("Example:", sense.example())
else:
    print("No suitable sense found.")