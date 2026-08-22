import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser

# Download required resources once
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")

words = word_tokenize(sentence)

tags = pos_tag(words)

# Grammar for noun phrases
grammar = """
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

parser = RegexpParser(grammar)

tree = parser.parse(tags)

print("\nNoun Phrases:")

found = False

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        phrase = " ".join(word for word, tag in subtree.leaves())
        print("-", phrase)
        found = True

if not found:
    print("No noun phrases found.")