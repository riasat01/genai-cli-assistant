import os
from dotenv import load_dotenv
from google import genai
from history_manager import load_history, save_history
from google.genai import types
from tools import search_web
import logging
logging.basicConfig(filename="debug.log", level=logging.DEBUG)

load_dotenv()

client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents="Write a one-sentence welcome message for a CLI AI assistant.",
# )

# print(f"AI: {response.text}")
# print(f"Full response: {response}")




def main():
    my_system_instruction = (
        "You are a helpful, witty, and slightly sarcastic coding assistant "
        "who loves to give funny and easily understandable analogies to explain question or concepts and keeps answers concise."
    )

    saved_history = load_history()
    chat = client.chats.create(
        model="gemini-3.6-flash", 
        history=saved_history,
        config=types.GenerateContentConfig(
            system_instruction=my_system_instruction,
            temperature=0.7,
            tools=[search_web],
            automatic_function_calling=types.AutomaticFunctionCallingConfig(maximum_remote_calls=3)
        )
    )
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

        if response.function_calls:
            print(f"\n⚙️ Tool Call Detected: {response.function_calls}\n")
        
        print(f"\nAI: {response.text}\n")

        save_history(chat)

if __name__ == "__main__":
    main()