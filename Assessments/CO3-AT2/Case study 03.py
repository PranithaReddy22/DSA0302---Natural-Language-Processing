words = [
    ["economic", "JJ"],
    ["growth", "NN"],
    ["increases", "NNS"],
    ["employment", "NN"]
]


for i in range(1, len(words)):
    if words[i][1] == "NNS" and words[i-1][1] == "NN":
        words[i][1] = "VBZ"

print("Corrected tags:", words)

freq = [120, 450, 210, 380]
total = sum(freq)

print("Frequency distribution:")

for f in freq:
    print(round(f / total, 3))