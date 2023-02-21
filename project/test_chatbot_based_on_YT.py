from chatterbot import corpus
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import filters


import pyttsx3

converter = pyttsx3.init()
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.7)


import speech_recognition as sr
import os



chatty = ChatBot("Chatty", 
                 storage_adapter = "chatterbot.storage.SQLStorageAdapter", 
                 logic_adapter = ["chatterbot.logic.MathematicalEvaluation",
                                  "chatterbot.logic.TimeAdapter",
                                  "chatterbot.logic.BestMatch",
                                  {
                                    'import_path' : 'chatterbot.logic.BestMatch',
                                    'default_response' : "Sorry, I'm not picking up what you're putting down",
                                    "maximum_similarity_threshold" : 0.90
                                  }
                                ],
                 database_uri = "sqlite:///database.sqlite3",
                 filters=[filters.get_recent_repeated_responses]) # This might not actually be doing anything
                                                                  # but I got it from the Chatterbot docs

trainer = ListTrainer(chatty)
training_data = open("/Users/joshuaroussak/Desktop/Chatthew/project/CURRENT_DATA/MyTrainer.yml").read().splitlines()
## ADD THE OTHER TRAINING DATA FROM chat_old.py !!!!!!!
#####
######
#######

#Training the corpus
CorpusTrainer = ChatterBotCorpusTrainer(chatty)
##################################CorpusTrainer.train("chatterbot.corpus.english")

"""
name = input("Enter your name: ")
print("Welcome, " + name)
"""

exit_cons = ["bye","goodbye","exit","quit","end"]

possible_voices = ["alex", "daniel", "fred", "rishi"]

"""
voices = converter.getProperty('voices')
  
for voice in voices:
    # to get the info. about various voices in our PC 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)

"""
converter.setProperty('voice', "com.apple.speech.synthesis.voice.rishi")
converter.setProperty('rate', 200)

def check_for_exit(exit_case, input):
   for w in exit_case: 
      if w in input:
        #print("Chatty: Alright, see you later, alligator!")
        print("Chatty: Alright, see you later, alligator!")
        converter.say("Alright, see you later, alligator!")
        converter.runAndWait()
        return True
      #print("A")

# 2/20/23 - DO I NEED TO DO THIS IN ORDER FOR THE SPEECH_TO_TEXT FUNCTION TO RETURN TEXT LIKE IT DOES IN chat_old.py ????????!!!

"""
class chattybot():
   def __init__(self, s2t):
      self.s2t = s2t
   
   #@staticmethod
   #@classmethod
"""
def speech_to_text():
  recognizer = sr.Recognizer()
  #recognizer.adjust_for_ambient_noise(sr.Microphone(device_index=0))
  #with sr.Microphone(sr.Microphone.list_microphone_names()[0]) as mic:
  with sr.Microphone(device_index=0) as mic:
      recognizer.adjust_for_ambient_noise(mic)
      print("listening...")
      #sr.adjust_for_ambient_noise(mic, duration=5)
      #print("WORKING SO FAR")
      audio = recognizer.listen(mic, timeout = 5)
      returned_audio = recognizer.recognize_google(audio)
      return str(returned_audio)

"""
def speech_to_text():
        recognizer = sr.Recognizer(self)
        #recognizer.adjust_for_ambient_noise(sr.Microphone(device_index=0))
        #with sr.Microphone(sr.Microphone.list_microphone_names()[0]) as mic:
        with sr.Microphone(device_index=0) as mic:
            recognizer.adjust_for_ambient_noise(mic)
            print("listening...")
            #sr.adjust_for_ambient_noise(mic, duration=5)
            #print("WORKING SO FAR")
            audio = recognizer.listen(mic, timeout = 5)
            return audio
"""

if __name__ == "__main__":

  name = input("Enter your name: ")
  print("Welcome, " + name)


  #charles = chattybot(s2t = "test")

  while True:
    #request = input(name + ": ").lower() #Adding .lower() is my touch
    
    # Gets the user's speech input
    #request = str(speech_to_text())
    request = speech_to_text()

    print(name + ":", request)

    #if request in exit_cons:
    if check_for_exit(exit_cons, request):
      break

    
    response = str(chatty.get_response(request))
    print("Chatty:", response)
    converter.say(response)
    converter.runAndWait()
