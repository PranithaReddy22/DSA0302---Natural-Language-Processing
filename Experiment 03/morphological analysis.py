import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download tokenizer (run once)
nltk.download('punkt')

text = "The students are studying computers and playing games."

# Tokenize the text
words = word_tokenize(text)

# Create stemmer object
ps = PorterStemmer()

print("Original Words\tStemmed Words")
for word in words:
    print(word, "\t\t", ps.stem(word))