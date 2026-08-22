import nltk
nltk.download("wordnet")

from nltk.corpus import wordnet

word = "bank"

for syn in wordnet.synsets(word):
    print(syn.name())
    print(syn.definition())