# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot("Megastore")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
   "chatterbot.corpus.english"
)

exit_conditions = (":q", "bye", "Bye")
while True:
    query = input("> ")
    if query in exit_conditions:
        print('Bot: Bye')
        break
    else:
        response = chatbot.get_response(query)
        print('Bot:',response)
