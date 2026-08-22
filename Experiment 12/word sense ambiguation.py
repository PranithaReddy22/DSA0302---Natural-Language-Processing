grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]]
}

def earley(words):
    chart = [set() for _ in range(len(words) + 1)]
    chart[0].add(("S", tuple(grammar["S"][0]), 0, 0))

    for i in range(len(words) + 1):
        changed = True
        while changed:
            changed = False
            for lhs, rhs, dot, start in list(chart[i]):
                if dot < len(rhs):
                    symbol = rhs[dot]

                    if symbol in grammar:
                        for rule in grammar[symbol]:
                            item = (symbol, tuple(rule), 0, i)
                            if item not in chart[i]:
                                chart[i].add(item)
                                changed = True
                    elif i < len(words) and symbol == words[i]:
                        chart[i + 1].add(
                            (lhs, rhs, dot + 1, start)
                        )

                else:
                    for item in list(chart[start]):
                        l, r, d, s = item
                        if d < len(r) and r[d] == lhs:
                            new_item = (l, r, d + 1, s)
                            if new_item not in chart[i]:
                                chart[i].add(new_item)
                                changed = True

    return any(
        lhs == "S" and dot == len(rhs) and start == 0
        for lhs, rhs, dot, start in chart[len(words)]
    )

print(earley("the cat sees the dog".split()))