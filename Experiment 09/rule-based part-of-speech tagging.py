import re


sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nPOS Tags:")

for word in words:
    if re.fullmatch(r"\d+", word):
        tag = "CD"    
    elif re.fullmatch(r".*ing", word):
        tag = "VBG"     
    elif re.fullmatch(r".*ed", word):
        tag = "VBD"     
    elif re.fullmatch(r".*ly", word):
        tag = "RB"      
    elif re.fullmatch(r".*ous|.*ful|.*able|.*ive", word):
        tag = "JJ"      
    else:
        tag = "NN"      

    print(word, "->", tag)