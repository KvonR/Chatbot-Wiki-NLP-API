from utils import fetch_wikipedia_summary, log_chat

import random

def chatbot_response(user_input):
    """
    Provides a response based on predefined keywords or fetches data from Wikipedia.
    """
    responses = {
        "hello": [
            "Hi there! How can I help?",
            "Hello! What’s on your mind?",
            "Hey! How can I assist you today?",
        ],
        "hi": [
            "Hi there! Need any assistance?",
            "Hello! What can I do for you?",
            "Hey there! Feel free to ask anything.",
        ],
        "bye": [
            "Goodbye! Have a fantastic day!",
            "See you later! Take care.",
            "Bye! Let me know if you need help again.",
        ],
        "help": [
            "Sure! Ask me anything you'd like.",
            "I’m here to help! What do you need?",
            "Go ahead, I’ll do my best to assist.",
        ],
    }

    user_input = user_input.lower()

    # Check if the input matches any keyword
    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    # Use Wikipedia integration for specific queries
    return fetch_wikipedia_summary(user_input)

if __name__ == "__main__":
    print("Chatbot: Hello! Ask me anything or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Get the bot's response
        response = chatbot_response(user_input)

        # Print the bot's response
        print(f"Chatbot: {response}")

        # Log the conversation
        log_chat(user_input, response)
