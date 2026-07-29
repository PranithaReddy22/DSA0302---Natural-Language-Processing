import random
from collections import defaultdict


text = """
Natural language processing is a field of artificial intelligence.
Natural language processing enables computers to understand human language.
Artificial intelligence is transforming the world.
"""


text = text.lower().replace(".", "")
words = text.split()


bigram_model = defaultdict(list)

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    bigram_model[current_word].append(next_word)

def generate_text(start_word, length=15):
    if start_word not in bigram_model:
        return "Start word not found in the model."

    result = [start_word]
    current_word = start_word

    for _ in range(length - 1):
        next_words = bigram_model.get(current_word)
        if not next_words:
            break
        current_word = random.choice(next_words)
        result.append(current_word)

    return " ".join(result)


start = "natural"
generated = generate_text(start, 15)

print("Generated Text:")
print(generated)