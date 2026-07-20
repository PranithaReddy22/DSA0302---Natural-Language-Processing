import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# List of words
words = ["playing", "studies", "running", "happily", "computers"]

print("Original Word\tStemmed Word")
for word in words:
    print(word, "\t", ps.stem(word))