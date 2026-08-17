import pandas as pd
import re
from nltk.stem import PorterStemmer

# Create Porter Stemmer
ps = PorterStemmer()

# Load BBC News dataset
data = pd.read_csv("BBCNews.csv")

# Function to stem complete text
def stem_text(text):
    words = re.findall(r'\b[a-zA-Z]+\b', str(text).lower())
    stemmed_words = []

    for word in words:
        stemmed_words.append(ps.stem(word))

    return " ".join(stemmed_words)


# Apply stemming to the Text column
data["Processed"] = data["Text"].apply(stem_text)

# Display original and stemmed text
print("ORIGINAL AND STEMMED TEXT")
print("--------------------------")

print(data[["Text", "Processed"]].head())


# 20 words for error analysis
words = [
    "organization",
    "organizer",
    "organizing",
    "organized",
    "organizations",
    "running",
    "runner",
    "runs",
    "studies",
    "studied",
    "studying",
    "happiness",
    "happily",
    "connection",
    "connected",
    "connectivity",
    "national",
    "relational",
    "traditional",
    "analysis"
]

print("\nORIGINAL WORD -> STEM")
print("----------------------")

for word in words:
    print(word, "->", ps.stem(word))