import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> VP

VP -> V NP
VP -> V NP PP

NP -> Det N
NP -> Det N PP

PP -> P NP

V -> 'show'

Det -> 'the' | 'last'

N -> 'transactions' | 'card' | 'month'

P -> 'with' | 'from'
""")

parser = nltk.ChartParser(grammar)

sent = "show the transactions with the card from last month".split()

for tree in parser.parse(sent):
    print(tree)
    tree.pretty_print()