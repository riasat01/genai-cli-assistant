import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a one-sentence welcome message for a CLI AI assistant.",
)

print(f"AI: {response.text}")
print(f"Full response: {response}")