import wikipedia
from datetime import datetime
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")

# Ensure required NLTK resources are downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

def process_query(query):
    """
    Processes the user input by tokenising and removing stopwords.
    """
    tokens = word_tokenize(query.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Debugging: Print the original and processed queries
    print(f"Original Query: {query}")
    print(f"Filtered Tokens: {filtered_tokens}")
    
    return ' '.join(filtered_tokens)

def fetch_wikipedia_summary(query):
    """
    Fetches a summary of the given query from Wikipedia, handling errors gracefully.
    """
    try:
        processed_query = process_query(query)
        print(f"Processed Query: {processed_query}")  # Debugging line

        # Skip queries that are too vague
        if len(processed_query.split()) < 2:
            return "That query seems too vague. Can you provide more details?"

        # Fetch a summary from Wikipedia
        summary = wikipedia.summary(processed_query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        suggestions = e.options[:5]
        return f"Your query is ambiguous. Did you mean one of these? {', '.join(suggestions)}"
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that topic. Please try being more specific."
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Something went wrong. Please try again later."

def log_chat(user_input, bot_response, log_file="chat_log.txt"):
    """
    Logs the conversation to a file with timestamps, using UTF-8 encoding.
    """
    with open(log_file, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] User: {user_input}\n")
        file.write(f"[{timestamp}] Bot: {bot_response}\n")
        file.write("\n")
