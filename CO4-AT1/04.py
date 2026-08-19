sentences = {
    "Doctor prescribed medicine to patient": {
        "Doctor": "Agent",
        "medicine": "Theme",
        "patient": "Recipient"
    },

    "Patient reported severe headache": {
        "Patient": "Experiencer",
        "headache": "Symptom"
    },

    "Nurse monitored patient": {
        "Nurse": "Agent",
        "patient": "Theme"
    },

    "Medicine reduced blood pressure": {
        "Medicine": "Cause",
        "blood pressure": "Theme"
    }
}

for sentence, roles in sentences.items():
    print("\nSentence:", sentence)

    for word, role in roles.items():
        print(word, "->", role)