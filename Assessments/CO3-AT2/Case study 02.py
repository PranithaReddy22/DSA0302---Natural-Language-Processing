# HMM probabilities

VB = 0.6 * 0.5
NN = 0.4 * 0.5

print("Book as VB:", VB)
print("Book as NN:", NN)

if VB > NN:
    print("HMM chooses: VB")
else:
    print("HMM chooses: NN")