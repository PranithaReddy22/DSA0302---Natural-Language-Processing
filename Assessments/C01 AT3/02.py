# DFA for strings ending with "ab"

# Transition table
transitions = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

initial_state = 'q0'
final_state = 'q2'

# Number of input strings
n = int(input("Enter number of strings: "))

for i in range(n):
    string = input("Enter string: ")

    state = initial_state

    for ch in string:
        if ch in transitions[state]:
            state = transitions[state][ch]
        else:
            state = None
            break

    if state == final_state:
        print("Accepted")
    else:
        print("Rejected")