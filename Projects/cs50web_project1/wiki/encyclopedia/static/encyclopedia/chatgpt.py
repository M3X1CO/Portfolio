import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You:")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)