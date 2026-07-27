import re

text = """Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing"""

while True:
    print("\n----- MENU -----")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
        print("Date:", result)

    elif choice == "2":
        result = re.findall(r"\b[6-9]\d{9}\b", text)
        print("Phone Number:", result)

    elif choice == "3":
        result = re.findall(r"#\w+", text)
        print("Hashtag:", result)

    elif choice == "4":
        result = re.findall(r"@\w+", text)
        print("Mention:", result)

    elif choice == "5":
        prefix = input("Enter prefix: ")
        result = re.findall(r"\b" + re.escape(prefix) + r"\w*", text, re.IGNORECASE)
        print("Prefix Matches:", result)

    elif choice == "6":
        suffix = input("Enter suffix: ")
        result = re.findall(r"\b\w*" + re.escape(suffix) + r"\b", text, re.IGNORECASE)
        print("Suffix Matches:", result)

    elif choice == "7":
        word = input("Enter word: ")
        result = re.findall(r"\b" + re.escape(word) + r"\b", text, re.IGNORECASE)

        if result:
            print("Word Found:", result)
        else:
            print("Word Not Found")

    elif choice == "8":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")