import tkinter as tk
from chatbot import chatbot_response  # Correct import from chatbot.py

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        
        # Chat display area
        self.chat_display = tk.Text(root, state='disabled', width=80, height=20, bg="lightyellow", font=("Arial", 12))
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Input area
        self.user_input = tk.Entry(root, width=60, font=("Arial", 12))
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        # Send button
        self.send_button = tk.Button(root, text="Send", width=15, command=self.send_message, bg="lightblue", font=("Arial", 12))
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

    def send_message(self):
        """
        Handles sending user input and displaying bot responses.
        """
        user_message = self.user_input.get().strip()  # Get user input
        if not user_message:
            return  # Ignore empty input

        # Display user message in the chat display
        self.display_message("You", user_message)
        self.user_input.delete(0, tk.END)  # Clear the input box

        # Get the bot's response
        bot_message = chatbot_response(user_message)
        self.display_message("Chatbot", bot_message)

    def display_message(self, sender, message):
        """
        Displays a message in the chat display area.
        """
        self.chat_display.config(state='normal')  # Enable editing to insert text
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.config(state='disabled')  # Disable editing to prevent user from modifying chat
        self.chat_display.see(tk.END)  # Scroll to the bottom

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
