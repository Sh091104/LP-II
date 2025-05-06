import random

def get_bot_response(user_msg):
    user_msg = user_msg.lower()

    # Greetings and farewells
    greetings = ['hi', 'hello', 'hey']
    farewells = ['bye', 'goodbye', 'see you']

    # Common questions
    questions = ['how are you', 'what is your name', 'what can you do']

    # Responses to different situations
    if any(greet in user_msg for greet in greetings):
        return random.choice(["Hello!", "Hey there!", "Hi! How can I assist you?"])
    
    elif 'how are you' in user_msg:
        return "I'm doing well, thank you for asking! How are you?"

    elif 'your name' in user_msg:
        return "I'm ChatBot, here to assist you."

    elif 'what can you do' in user_msg:
        return "I can assist with basic conversations. Feel free to ask me anything!"

    elif any(bye in user_msg for bye in farewells):
        return random.choice(["Goodbye!", "See you later!", "Take care!"])

    elif 'thank you' in user_msg or 'thanks' in user_msg:
        return "You're welcome! Let me know if you need anything else."

    elif 'how old are you' in user_msg:
        return "I don't have an age, as I'm just a bot!"

    elif 'where are you from' in user_msg:
        return "I'm from the cloud! I exist in the digital world."
        
    elif 'what do you like' in user_msg:
        return "i love talking to you."

    elif 'what do you like' in user_msg:
        return "I don't have preferences, but I enjoy helping you with questions!"

    else:
        return "Sorry, I didn't quite understand that. Can you try asking something else?"

def main():
    print("Bot: Hello! I'm ChatBot. Type something to start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Bot: Goodbye! Have a nice day.")
            break

        bot_reply = get_bot_response(user_input)
        print("Bot:", bot_reply)

if __name__ == "__main__":
    main()