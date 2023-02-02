import speech_recognition as sr

# get audio from the microphone
# 
# 

                                                                
r = sr.Recognizer()                    
keyword = "hello" 

with sr.Microphone() as source:
    print('Please start speaking..\n')
    while True: 
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if keyword.lower() in text.lower():
                print('Keyword detected in the speech.')
        except Exception as e:
            print('Please speak again.')






"""
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    if r.recognize_google(audio)) == keyword:
        myfunction()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
"""