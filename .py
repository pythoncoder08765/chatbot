# Task 4: Basic Chatbot (rule-based)

def reply(user_text: str) -> str:
    msg = user_text.strip().lower()

    # Normalize a few common variants
    greetings = {"hi", "hello", "hey", "hey there"}
    how_are_you = {
        "how are you", "how r u", "how are u", "how’s it going", "how are you?"
    }
    bye_words = {"bye", "goodbye", "see you", "see ya", "exit", "quit"}

    if msg in greetings:
        return "Hi!"
    elif msg in how_are_you or msg.startswith("how are you"):
        return "I'm fine, thanks!"
    elif msg in bye_words:
        return "Goodbye!"
    else:
        # Default fallback
        return "I can reply to: 'hello', 'how are you', or 'bye'."

def chat():
    print("Chatbot ready. Type 'bye' to end.\n")
    while True:
        user = input("You: ")
        bot = reply(user)
        print("Bot:", bot)
        if bot == "Goodbye!":
            break

if __name__ == "__main__":
    chat()
