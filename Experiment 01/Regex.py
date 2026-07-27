import re

print("Program Started")

text = input("Enter a sentence: ")

print("You entered:", text)

pattern1 = input("Enter the pattern to match at the beginning: ")
pattern2 = input("Enter the pattern to search: ")

match = re.match(pattern1, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")

search = re.search(pattern2, text)

if search:
    print("Search found:", search.group())
else:
    print("Pattern not found")