from collections import Counter
import math
import re

train = """
the student is studying python
the student is learning machine learning
the teacher is teaching python
python is a programming language
machine learning is useful
"""

test = """
the student is studying python
the teacher is learning python
"""

train = re.findall(r'\b[a-z]+\b', train.lower())
test = re.findall(r'\b[a-z]+\b', test.lower())

uni = Counter(train)
bi = Counter(zip(train, train[1:]))
tri = Counter(zip(train, train[1:], train[2:]))

def entropy(probabilities):
    values = [p for p in probabilities if p > 0]
    return -sum(math.log2(p) for p in values) / len(values)

# Unigram
up = [uni[w] / len(train) for w in test if uni[w]]
u_entropy = entropy(up)

# Bigram
bp = []
for a, b in zip(test, test[1:]):
    if bi[(a, b)] and uni[a]:
        bp.append(bi[(a, b)] / uni[a])

b_entropy = entropy(bp)

# Trigram
tp = []
for a, b, c in zip(test, test[1:], test[2:]):
    if tri[(a, b, c)] and bi[(a, b)]:
        tp.append(tri[(a, b, c)] / bi[(a, b)])

t_entropy = entropy(tp)

print("Unigram Entropy :", round(u_entropy, 4))
print("Bigram Entropy  :", round(b_entropy, 4))
print("Trigram Entropy :", round(t_entropy, 4))

print("\nInterpretation:")
print("Lower entropy  -> More predictable")
print("Higher entropy -> Less predictable")