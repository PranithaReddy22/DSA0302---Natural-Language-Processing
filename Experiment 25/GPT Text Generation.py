from openai import OpenAI

client = OpenAI()

prompt = input("Enter a prompt: ")

response = client.responses.create(
    model="gpt-5.6",
    input=prompt
)

print("\nGenerated Text:")
print(response.output_text)