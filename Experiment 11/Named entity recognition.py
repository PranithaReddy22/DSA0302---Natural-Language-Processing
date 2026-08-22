grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]]
}

def parse(symbols, words):
    if not symbols:
        return len(words) == 0

    first = symbols[0]

    if first not in grammar:
        return words and first == words[0] and parse(symbols[1:], words[1:])

    for rule in grammar[first]:
        if parse(rule + symbols[1:], words):
            return True
    return False

sentence = "the cat sees the dog".split()
print("Accepted:", parse(["S"], sentence))