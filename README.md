# Local Chatbot
It allows interactive conversations with an AI assistant, logs conversations to a file, filters inappropriate content, and can summarize long chats automatically.

**Technologies:**`Python 3.10`,`Ollama TinyLlama** model`,Standard Python libraries: `time`, `os`

## How It Works

1. The user inputs a message to the chatbot.
2. Messages are stored in memory and logged to `conversation.txt`.
3. Messages containing blocked words (`violence`, `drugs`, `hate`) are filtered out.
4. The chatbot sends messages to the Ollama TinyLlama model and receives a response.
5. If the conversation grows too long, the bot generates a brief summary to keep context manageable.

## Usage

Run the chatbot with:

```bash
python local-chatbot.py
In the chatbot, you can use the following commands:

/help → Show commands

/clear → Clear conversation history

/exit → Exit the chatbot
```
## Requirements
Python 3.10 or higher

Ollama CLI installed and configured
