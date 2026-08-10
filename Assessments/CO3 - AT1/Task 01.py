from collections import Counter
import re

corpus = """
the student is studying python
the student is learning machine learning
the student is reading a book
the student is writing an assignment
the teacher is teaching python
the teacher is reading a book
python is a programming language
machine learning is useful
"""


words = re.findall(r'\b[a-z]+\b', corpus.lower())


uni = Counter(words)
bi = Counter(zip(words, words[1:]))
tri = Counter(zip(words, words[1:], words[2:]))

def predict(sentence, n):
    w = re.findall(r'\b[a-z]+\b', sentence.lower())
    result = []

    if n == 1:
        for word, count in uni.items():
            result.append((word, count / len(words)))

    elif n == 2:
        prev = w[-1]
        total = uni[prev]
        for (a, b), count in bi.items():
            if a == prev:
                result.append((b, count / total))

    elif n == 3:
        a, b = w[-2:]
        total = bi[(a, b)]
        for (x, y, z), count in tri.items():
            if x == a and y == b:
                result.append((z, count / total))

    return sorted(result, key=lambda x: x[1], reverse=True)[:5]


n = int(input("Enter N (1/2/3): "))
sentence = input("Enter incomplete sentence: ")

print("\nTop-5 predictions:")
for word, prob in predict(sentence, n):
    print(word, "->", round(prob, 4))


print("\nUnseen bigram probability:",
      bi[("student", "elephant")] / uni["student"])