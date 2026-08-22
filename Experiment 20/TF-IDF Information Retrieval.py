from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Number of documents
n = int(input("Enter number of documents: "))

documents = []

for i in range(n):
    document = input(f"Enter document {i + 1}: ")
    documents.append(document)

query = input("Enter search query: ")

# Create TF-IDF matrix
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform([query])

# Calculate similarity
similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

print("\nDocument Ranking:")

ranking = similarities.argsort()[::-1]

for index in ranking:
    print(
        f"Document {index + 1}: "
        f"Similarity = {similarities[index]:.4f}"
    )