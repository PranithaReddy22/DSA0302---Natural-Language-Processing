from collections import Counter
import re

corpus = """
the student is studying python
the student is learning machine learning
the student is reading books
the teacher is teaching python
the teacher is learning machine learning
python is a programming language
machine learning is useful
"""

words = re.findall(r'\b[a-z]+\b', corpus.lower())

uni = Counter(words)
bi = Counter(zip(words, words[1:]))
tri = Counter(zip(words, words[1:], words[2:]))

N = len(words)

def unigram(w):
    return uni[w] / N

def bigram(a, b):
    return bi[(a, b)] / uni[a] if uni[a] else 0

def trigram(a, b, c):
    return tri[(a, b, c)] / bi[(a, b)] if bi[(a, b)] else 0

def backoff(a, b, c):
    p = trigram(a, b, c)

    if p > 0:
        return p

    p = bigram(b, c)

    if p > 0:
        return p

    return unigram(c)

def interpolation(a, b, c):
    return (0.5 * trigram(a, b, c) +
            0.3 * bigram(b, c) +
            0.2 * unigram(c))

sentence = input("Enter incomplete sentence: ")
w = sentence.lower().split()

a, b = w[-2], w[-1]

results = []

for c in uni:
    bp = backoff(a, b, c)
    ip = interpolation(a, b, c)
    results.append((c, bp, ip))

results.sort(key=lambda x: x[1], reverse=True)

print("\nBackoff Predictions:")
for word, bp, ip in results[:5]:
    print(word, "->", round(bp, 4))

results.sort(key=lambda x: x[2], reverse=True)

print("\nDeleted Interpolation Predictions:")
for word, bp, ip in results[:5]:
    print(word, "->", round(ip, 4))