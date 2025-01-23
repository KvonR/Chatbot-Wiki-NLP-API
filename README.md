# Chatbot Project

An interactive chatbot built with Python, featuring both a command-line interface (CLI) and a graphical user interface (GUI). The chatbot uses Wikipedia to answer questions, logs conversations to a file, and processes natural language with basic NLP techniques.

---

## Features

- **Chatbot Functionality**: Responds to greetings, farewells, and general help requests with predefined responses. For other queries, it fetches data from Wikipedia.
- **Graphical User Interface (GUI)**: A simple and user-friendly interface created using `Tkinter`.
- **Conversation Logging**: Saves all interactions to `chat_log.txt` with timestamps.
- **Basic NLP**: Cleans and processes user input using the `nltk` library.

---

## Setup and Requirements

### Prerequisites

1. Python 3
2. Install the required libraries by running:

```bash
pip install -r requirements.txt
```

### NLTK Setup

The chatbot uses NLTK's `punkt` and `stopwords` resources. To download them, run:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## Project Structure

```
chatbot_project/
├── chatbot.py         # CLI-based chatbot logic
├── chatbot_gui.py     # GUI-based chatbot implementation
├── utils.py           # Helper functions (Wikipedia integration, logging, NLP)
├── chat_log.txt       # Log file for chat history (auto-created)
└── requirements.txt   # List of dependencies
```

---

## How to Use

### Command-Line Interface (CLI)

1. Open a terminal in the project directory.
2. Start the chatbot with:
   ```bash
   python chatbot.py
   ```
3. Type your message and press Enter. Type 'bye' to exit.

### Graphical User Interface (GUI)

1. Open a terminal in the project directory.
2. Launch the GUI with:
   ```bash
   python chatbot_gui.py
   ```
3. Interact with the chatbot using the input box and Send button.

---

## Example Usage

### CLI Interaction

```
Chatbot: Hello! Ask me anything or type 'bye' to exit.
You: Hello
Chatbot: Hi there! How can I help?
You: Who is Elon Musk?
Chatbot: Elon Musk is a business magnate and the founder of Tesla and SpaceX.
You: Bye
Chatbot: Goodbye! Have a fantastic day!
```

### GUI Interaction

1. Launch the GUI and type "Who is Albert Einstein?" into the input box.
2. Click "Send" and see the response in the chat window.

---

## Key Features

### 1. Wikipedia Integration

Fetches live data to provide accurate and dynamic responses.

### 2. Logging

Every conversation is saved to `chat_log.txt` with timestamps for later review.

### 3. Basic NLP

Processes user input by removing unnecessary words (stopwords) and cleaning the text.

### 4. Simple GUI

Built with `Tkinter`, the interface provides an easy way to interact with the chatbot.

---

## Future Improvements

- Add sentiment analysis to better understand user emotions.
- Integrate GPT models for more intelligent and conversational responses.
- Deploy the chatbot as a web app using Flask or FastAPI.

---

## Author

This project demonstrates Python skills in API integration, file handling, and GUI development. It is designed as an excellent starting point for creating more advanced chatbot applications.
