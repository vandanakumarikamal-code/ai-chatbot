from huggingface_hub import InferenceClient

client = InferenceClient()

print("Vandana's Ai Chatbot")
print("Type 'exit' to stop")

while True:
    message = input("You: ")

    if message.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": message}
        ],
        max_tokens=200
    )

    print("AI:", response.choices[0].message.content)