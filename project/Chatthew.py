import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Stuff for speech_to_text_to_speech
import pyttsx3

converter = pyttsx3.init()
converter.setProperty('voice', "com.apple.speech.synthesis.voice.rishi")
converter.setProperty('rate', 190)
converter.setProperty('volume', 0.5)

import speech_recognition as sr

def speech_to_text():
  recognizer = sr.Recognizer()
  #recognizer.adjust_for_ambient_noise(sr.Microphone(device_index=0))
  #with sr.Microphone(sr.Microphone.list_microphone_names()[0]) as mic:
  with sr.Microphone(device_index=0) as mic:
      recognizer.adjust_for_ambient_noise(mic, duration = .25)
      print("listening...")
      #sr.adjust_for_ambient_noise(mic, duration=5)
      #print("WORKING SO FAR")
      ######OLD WAY: audio = recognizer.listen(mic, timeout = 5)
      audio = recognizer.listen(mic,5,4)
      try:
          returned_audio = recognizer.recognize_google(audio)
      except:
          returned_audio = "ERROR"
      return str(returned_audio)





device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#with open("/Users/joshuaroussak/Desktop/Chatthew/project/CURRENT_DATA/CopiedFromIntents.json", "r") as f:
with open("/Users/joshuaroussak/Desktop/Chatthew/project/intent-based-dataset.json", "r") as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Chatthew"
print("Let's chat! Say 'quit' or 'goodbye' to exit")

"""
# Printed output
while True:
    sentence = input("You: ")
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)
    
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                print(f"{bot_name}: {(random.choice(intent['responses']))}")
    else:
        print(f"{bot_name}: I do not understand...")
"""
        
def get_input():
    try:
        input = speech_to_text()
        print("Me: " + input)
    except:
        print("FAIL!")
        raise Exception("Input error")
    """
    if sentence == "quit":
        raise Exception("Input error")"""
    return input
# Spoken output
def generate_response(sentence):
    # This code has been moved to the get_input() function
    """
    try:
        sentence = speech_to_text()
        print("Me: " + sentence)
    except:
        print("FAIL!")
        return
    if sentence == "quit":
        return
    """

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)
    
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    """
    if sentence == "quit":
        return"""

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
    else:
        response = "I do not understand"
    # This part that printed and spoke out the response has been moved to the start_chat(response) function, with this function 
    # now just returning a string response that it generates
    """
    print(f"{bot_name}: {response}")
    converter.say(response)
    converter.runAndWait()
    """
    return response

def say_response(r):
    if r == None:
        return
    print(f"{bot_name}: {r}")
    converter.say(r)
    converter.runAndWait()

def talk():
    while True:
        sentence = get_input()
        #if sentence == "quit" or sentence == 'goodbye':
        if "quit" in sentence or "goodbye" in sentence:
            message = "Ok, see you around"
            """
            print(f"Chatthew: {message}")
            converter.say(message)
            converter.runAndWait()"""
            say_response(message)
            break
        response = generate_response(sentence)
        say_response(response)




if __name__ == "__main__":
    talk()
    #while True:
"""
    try:
        sentence = speech_to_text()
        print("Me: " + sentence)
    except:
        print("FAIL!")
        break
    if sentence == "quit":
        break
"""

        # This functionality has been moved to talk()
"""
sentence = get_input()
response = generate_response(sentence)
start_chat(response)
"""
    #talk()
"""
    for intent in intents["intents"]:
        if tag == intent["tag"]:
            print(f"{bot_name}: {random.choice(intent['responses'])}")"""