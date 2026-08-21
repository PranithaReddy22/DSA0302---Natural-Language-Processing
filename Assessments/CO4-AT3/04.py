feature = {
    "subject_number": "singular",
    "verb_number": "singular"
}

verb = {
    "eat": ["Subject", "Object"],
    "sleep": ["Subject"]
}

print("Agreement:", feature["subject_number"] == feature["verb_number"])
print("Eat requires:", verb["eat"])