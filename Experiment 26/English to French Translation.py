from transformers import pipeline

# Create English-to-French translation pipeline
translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = input("Enter English text: ")

result = translator(text)

print("\nEnglish:")
print(text)

print("\nFrench:")
print(result[0]["translation_text"])