grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]]
}

def tree(symbol, words):
    if symbol not in grammar:
        return symbol, words.pop(0)

    for rule in grammar[symbol]:
        children = []
        backup = words[:]

        try:
            for x in rule:
                children.append(tree(x, words))
            return symbol, children
        except:
            words[:] = backup

sentence = "the cat sees the dog".split()
print(tree("S", sentence))