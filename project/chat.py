from chatterbot import ChatBot
#import nltk
#nltk.download('punkt')


#from collections.abc import Hashable


# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
#from chatterbot.trainers import ChatterBotCorpusTrainer
 
  
# Give a name to the chatbot “corona bot”
# and assign a trainer component.
chatbot=ChatBot('corona bot')
 
# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)
  
# Now let us train our bot with multiple corpus
#trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations" )


print(chatbot.get_response("How is it going?"))
""" 
response = chatbot.get_response('What is your Number')
print(response)
 
response = chatbot.get_response('Who are you?')
print(response)
"""