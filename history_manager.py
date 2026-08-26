import json
import os

HISTORY_FILE = "chat_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Failed to load history: {e}")
            return []
        return []

def save_history(chat_session):
    history_data = []
    for content in chat_session.get_history():
        role = content.role
        parts = [{"text": part.text} for part in content.parts if part.text]

        if parts:
            history_data.append({"role": role, "parts": parts})

    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history_data, f, indent=2)

    except Exception as e:
        print(f"⚠️ Failed to save history: {e}")
