queries = {
    "Apple accessories": "iPhone Charger",
    "Mouse wireless": "Bluetooth Mouse",
    "Java tutorial": "Coding Lessons",
    "Python course": "Software Development Training"
}
for q, result in queries.items():
    if "Apple" in q:
        sense = "Technology Brand"
    elif "Mouse" in q:
        sense = "Computer Device"
    else:
        sense = "Programming Language"
    print(q, "->", sense, "->", result)