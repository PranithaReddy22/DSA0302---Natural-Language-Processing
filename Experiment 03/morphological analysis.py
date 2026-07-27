import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Create Porter Stemmer object
ps = PorterStemmer()

# Take input from user
text = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(text)

print("\nOriginal Word\t\tStemmed Word")
print("-" * 35)

for word in words:
    print(f"{word}\t\t{ps.stem(word)}")