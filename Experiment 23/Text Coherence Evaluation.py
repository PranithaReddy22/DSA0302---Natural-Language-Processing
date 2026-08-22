from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = input("Enter a multi-sentence text: ")

sentences = [s.strip() for s in text.split('.') if s.strip()]

if len(sentences) < 2:
    print("Please enter at least two sentences.")
else:
    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(sentences)

    similarities = cosine_similarity(matrix)

    total = 0
    count = 0

    print("\nSentence Similarities:")

    for i in range(len(sentences) - 1):
        score = similarities[i][i + 1]

        print(
            f"Sentence {i + 1} ↔ Sentence {i + 2}: "
            f"{score:.4f}"
        )

        total += score
        count += 1

    coherence = total / count

    print(f"\nCoherence Score: {coherence:.4f}")

    if coherence >= 0.3:
        print("Text is relatively coherent.")
    else:
        print("Text has low coherence.")