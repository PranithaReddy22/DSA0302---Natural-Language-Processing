grammar = {
    "S": [(["NP", "VP"], 1.0)],
    "NP": [(["Det", "N"], 0.8)],
    "VP": [(["V", "NP"], 0.7)],
    "Det": [(["the"], 1.0)],
    "N": [(["cat"], 0.5), (["dog"], 0.5)],
    "V": [(["sees"], 1.0)]
}

def parse(symbol, words):
    if symbol not in grammar:
        return 1.0 if words and words[0] == symbol else 0

    total = 0

    for rule, prob in grammar[symbol]:
        if len(rule) == 1 and rule[0] in words:
            total += prob

    return total

print("Probability:", parse("N", ["cat"]))