import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents="Write a one-sentence welcome message for a CLI AI assistant.",
# )

# print(f"AI: {response.text}")
# print(f"Full response: {response}")




def main():
    chat = client.chats.create(model="gemini-3.6-flash")
    print("🤖 Gemini CLI Assistant Ready! (Type 'exit' or 'quit' to end)\n")

    while True:
        user_input = input("Me: ").strip()
        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        response = chat.send_message(user_input)
        print(f"\nAI: {response.text}\n")

if __name__ == "__main__":
    main()