import re
from collections import Counter

training = [
    ("the", "DT"), ("student", "NN"), ("is", "VBZ"),
    ("studying", "VBG"), ("python", "NN"),
    ("the", "DT"), ("teacher", "NN"), ("is", "VBZ"),
    ("teaching", "VBG"), ("python", "NN"),
    ("students", "NNS"), ("learn", "VB"),
    ("quickly", "RB"), ("good", "JJ")
]


tag_dict = {}

for word, tag in training:
    tag_dict.setdefault(word, []).append(tag)


def rule_based(words):
    result = []

    for w in words:
        if w in tag_dict:
            tag = Counter(tag_dict[w]).most_common(1)[0][0]
        elif w.endswith("ing"):
            tag = "VBG"
        elif w.endswith("ly"):
            tag = "RB"
        elif w.endswith("ed"):
            tag = "VBD"
        elif w.endswith("s"):
            tag = "NNS"
        else:
            tag = "NN"

        result.append((w, tag))

    return result



def transformation(tagged):
    result = tagged.copy()

    for i, (word, tag) in enumerate(result):

        if i > 0:
            previous = result[i - 1][1]

            # noun after pronoun/auxiliary -> verb
            if previous in ["PRP", "VB", "VBZ"] and tag == "NN":
                result[i] = (word, "VB")

    return result


sentence = input("Enter sentence: ")
words = re.findall(r'\b[a-z]+\b', sentence.lower())


rb = rule_based(words)

print("\nRule-Based Tagging:")
print(rb)


print("\nStochastic Tagging:")
stochastic = rule_based(words)
print(stochastic)


tb = transformation(stochastic)

print("\nTransformation-Based Tagging:")
print(tb)