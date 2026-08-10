words=["create","creates","creating"]

rules={
"create":("-","Base Form"),
"creates":("s","Third Person Singular"),
"creating":("ing","Present Participle")
}

print("-"*75)
print("{:<12}{:<10}{:<25}{:<12}{:<12}".format(
"Word","Suffix","Category","Root","Normalized"))
print("-"*75)

for word in words:
    suffix,category=rules[word]

    print("{:<12}{:<10}{:<25}{:<12}{:<12}".format(
    word,suffix,category,"create","create"))