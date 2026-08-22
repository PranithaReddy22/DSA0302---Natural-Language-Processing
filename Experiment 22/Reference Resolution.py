import re

text = input("Enter a text: ")

sentences = re.split(r'(?<=[.!?])\s+', text)

pronouns = {
    "he", "she", "it", "they", "him",
    "her", "them", "his", "their"
}

last_entity = None

print("\nResolved Text:")

for sentence in sentences:
    words = sentence.split()
    resolved_words = []

    for word in words:
        clean_word = re.sub(r'[^\w]', '', word)
        lower_word = clean_word.lower()

        if lower_word in pronouns and last_entity:
            punctuation = word[len(clean_word):]
            resolved_words.append(last_entity + punctuation)
        else:
            resolved_words.append(word)

            # Simple entity detection
            if clean_word and clean_word[0].isupper():
                last_entity = clean_word

    print(" ".join(resolved_words))