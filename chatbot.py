from chatterbot import ChatBot
import nltk

nltk.download('punkt_tab')

# Created ChatBot instance
chatbot = ChatBot("ChatBot")

# Created while loop for functionality and exit conditions
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🎮 {chatbot.get_response(query)}")