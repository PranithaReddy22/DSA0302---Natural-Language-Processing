import nltk

# Download required NLTK resources (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')


text = input("Enter a sentence: ")

# Tokenize the sentence into words
words = nltk.word_tokenize(text)


pos_tags = nltk.pos_tag(words)


print("\nPart-of-Speech Tags:")
for word, tag in pos_tags:
    print(word, "->", tag)