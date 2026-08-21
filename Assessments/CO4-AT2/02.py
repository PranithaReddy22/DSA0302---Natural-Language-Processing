import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> VP
VP -> V NP PP PP
NP -> Det N
NP -> Det N N
NP -> N
PP -> P NP
V -> 'book'
Det -> 'a'
N -> 'flight' | 'window' | 'seat' | 'delhi'
P -> 'to' | 'with'
""")

parser = nltk.ChartParser(grammar)

sentence = "book a flight to delhi with a window seat".split()

trees = list(parser.parse(sentence))

if trees:
    for tree in trees:
        print(tree)
        tree.pretty_print()
else:
    print("No parse tree found.")