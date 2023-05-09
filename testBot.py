import json
import nltk
from nltk.chat.util import Chat, reflections

with open('nlu.json', 'r') as file:
    intents = json.load(file)

pairs = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        pairs.append((pattern, intent['responses']))
        
class CustomChat(Chat):
    _quit_phrases = ("goodbye", "bye", "exit", "quit")
    _fallback_response = "I'm sorry, I don't understand. Could you please rephrase your question?"

    def converse(self, quit="goodbye"):
        user_input = ""
        while user_input.lower() != quit.lower():
            user_input = quit
            try:
                user_input = input("User: ")
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                response = self.respond(user_input.replace("User: ", ""))
                if response:
                    print("Chatzilla: " + response)
                    if self._quit_phrases and response.lower() in self._quit_phrases:
                        break
                else:
                    print("Chatzilla: " + self._fallback_response)

chatbot = CustomChat(pairs, reflections)

chatbot.converse()