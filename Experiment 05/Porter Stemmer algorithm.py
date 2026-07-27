from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# Take input from user
text = input("Enter words separated by space: ")

# Convert input string into list
words = text.split()

print("\nOriginal Word\tStemmed Word")
print("-" * 30)

for word in words:
    print(f"{word}\t\t{ps.stem(word)}")