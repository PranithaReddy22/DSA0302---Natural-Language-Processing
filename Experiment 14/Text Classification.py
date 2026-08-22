def agreement(sentence):
    words = sentence.lower().split()

    if words[0] in ["he", "she", "it"] and words[1] == "run":
        return False

    if words[0] in ["he", "she", "it"] and words[1] == "runs":
        return True

    if words[0] in ["they", "we"] and words[1] == "run":
        return True

    return False

print(agreement("She runs"))
print(agreement("They run"))