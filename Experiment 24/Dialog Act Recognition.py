def recognize_dialog_act(sentence):
    text = sentence.lower().strip()

    if text.endswith("?"):
        return "Question"

    if any(word in text for word in ["hello", "hi", "hey", "good morning"]):
        return "Greeting"

    if any(word in text for word in ["thank you", "thanks"]):
        return "Thanking"

    if any(word in text for word in ["please", "could you", "would you"]):
        return "Request"

    if any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Closing"

    if any(word in text for word in ["yes", "okay", "sure"]):
        return "Agreement"

    return "Statement"


sentence = input("Enter a dialog sentence: ")

act = recognize_dialog_act(sentence)

print("\nDialog Act:", act)