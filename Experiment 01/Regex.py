import re

text = "Welcome to Python Programming"

# Match pattern at the beginning
match = re.match("Welcome", text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")

# Search pattern anywhere in the text
search = re.search("Python", text)

if search:
    print("Search found:", search.group())
else:
    print("Pattern not found")