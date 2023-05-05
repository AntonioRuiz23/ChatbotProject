from chatterbot import Chatbot 

from chatterbot.trainer import ChatterBotCorpusTrainer

from nltk.tokenize import word_tokinize


chatbot = Chatbot("MyBot")

trainer = ChatterBotCorpusTrainer(chatbot)

def get_response(user_input):
    tokenized_input = word_tokinize(user_input)
    response = chatbot.get_response(user_input).text
    return response

while True:
    user_input = input("Usuario: ")
    if user_input == "adios" or user_input == "Adios":
        print("Bot: Adios")
        break
    response = get_response(user_input)
    print("Bot: "+response)