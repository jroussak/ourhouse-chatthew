#"""
import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer

from chatterbot.trainers import ListTrainer



###import nltk
###import ssl

"""
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
"""

#nltk.download()


#chatbot = ChatBot("FOR_TRAINING", storage_adapter = 'chatterbot.storage.SQLStorageAdapter', 
#database_uri = 'sqlite:///database.sqlite3')
chatbot = ChatBot("FOR_TRAINING")

exit_conditions = ("quit", "exit", "goodbye")

#trainer = ChatterBotCorpusTrainer(chatbot)
"""
trainer = UbuntuCorpusTrainer(chatbot)
stuff = trainer.download("https://www.kaggle.com/datasets/rtatman/ubuntu-dialogue-corpus?resource=download&select=Ubuntu-dialogue-corpus")
"""

#path = "./Desktop/project/MyTrainer.yml"

list_trainer = ListTrainer(chatbot)
source1 = "/Users/joshuaroussak/Desktop/project/CURRENT_DATA/MyTrainer.yml"
source2 = "/Users/joshuaroussak/Desktop/project/CURRENT_DATA/CopiedFromIntents.json"

source_file1 = open(source1, "r")
source_file2 = open(source2, "r")

source_data1 = source_file1.read().splitlines()
source_data2 = source_file2.read().splitlines()

list_trainer.train(source_data1)
list_trainer.train(source_data2)

# Note: Deleted "chatterbot.corpus.english.emotion" from this list because it returned "No, I am sober" to "what is your name"
"""
trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.botprofile", 
"chatterbot.corpus.english.computers", "chatterbot.corpus.english.food",
"chatterbot.corpus.english.gossip", "chatterbot.corpus.english.greetings", "chatterbot.corpus.english.health", 
"chatterbot.corpus.english.history", "chatterbot.corpus.english.humor", "chatterbot.corpus.english.literature", 
"chatterbot.corpus.english.money", "chatterbot.corpus.english.movies", "chatterbot.corpus.english.psychology", 
"chatterbot.corpus.english.science", "chatterbot.corpus.english.sports", "chatterbot.corpus.english.trivia")
"""
#trainer.train("chatterbot.corpus.english.conversations", "chatterbot.corpus.english.humor", "chatterbot.corpus.english.movies")
###trainer.train("chatterbot.corpus.english.trivia")

#trainer.train("Desktop/UBUNTU_JUNK/dialogueText_196.csv")

#trainer.train()

#trainer.train("chatterbot.corpus.english")
#trainer.train(*"./Desktop/ambignq_light/ambig_nq_yam.yml")
#trainer.train(*"Desktop/project/MyTrainer.yaml")

#import sys
#print(sys.version)


# Beginning of the AI
class ChatBot():
    def __init__(self, name, text):
        print("----- starting up", name, "-----")
        self.name = name
        self.text = text

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        #recognizer.adjust_for_ambient_noise(sr.Microphone(device_index=0))
        #with sr.Microphone(sr.Microphone.list_microphone_names()[0]) as mic:
        with sr.Microphone(device_index=0) as mic:
            recognizer.adjust_for_ambient_noise(mic)
            print("listening...")
            #sr.adjust_for_ambient_noise(mic, duration=5)
            #print("WORKING SO FAR")
            audio = recognizer.listen(mic, timeout = 5) # SOMETHING WRONG WITH LISTEN ?????
            #print("WORKING SO FAR 2")
        
        """
        self.text = recognizer.recognize_google(audio)
        print("me --> ", self.text)
        """

        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("me -->  ERROR")
        
        
    @staticmethod
    def text_to_speech(text):
        print("Chatthew --> ", text)
        speaker = gTTS(text = text, lang = "en", slow=False)
        speaker.save("res.mp3")
        os.system("afplay res.mp3")
        os.remove("res.mp3")


    def wake_up(self, text):
        #if self.name in text.lower():
        if self.name in text:
            return True
        else:
            return False




# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="test", text="test")
    
    #trainer = ChatterBotCorpusTrainer(ai)
    #trainer.train("chatterbot.corpus.english.conversations", "chatterbot.corpus.english.humor", "chatterbot.corpus.english.movies")


    while True:
        """
        # Gets your input from speech and stores it as text in ai.text
        ai.speech_to_text()

        # Sets var to your input as text.lower()
        var = ai.text.lower()

        if var in exit_conditions:
            ai.text_to_speech("Talk to you later")
            break
        
        #var = input("ENTER SOMETHING: ")

        # Uses the ai.wakeup() function with your input to see if its name is in your input (If its name is there, return True; else, False)
        if ai.wake_up(var) == True:
            res = "Hi! My name is Chatthew the AI. What's up?"
        elif "what's up" in var:
            res = "Not much. How about you?"
        else:
            res = str(chatbot.get_response(var))
        #res = "test"
        ai.text_to_speech(res)
        """
        
        var = input("Say something: ").lower()
        if ai.wake_up(var):
                print("YES")
        if var in exit_conditions:
                break


        #inp = input("Say something: ")
        print("Aviel: " + str(chatbot.get_response(var)))
