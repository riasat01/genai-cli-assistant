import os
from dotenv import load_dotenv
from google import genai
from history_manager import load_history, save_history

load_dotenv()

client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents="Write a one-sentence welcome message for a CLI AI assistant.",
# )

# print(f"AI: {response.text}")
# print(f"Full response: {response}")




def main():
    saved_history = load_history()
    chat = client.chats.create(model="gemini-3.6-flash", history=saved_history)
    print("🤖 Gemini CLI Assistant Ready! (Type 'exit' or 'quit' to end)\n")

    if saved_history:
        print(f"📜 Loaded previous session ({len(saved_history)} messages).")

    while True:
        user_input = input("Me: ").strip()
        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        response = chat.send_message(user_input)
        print(f"\nAI: {response.text}\n")

        save_history(chat)

if __name__ == "__main__":
    main()