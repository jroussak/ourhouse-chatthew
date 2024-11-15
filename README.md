# Welcome to Chatthew, the conversational, speech-to-text-to-speech chatbot!

## Overview
This was a passion project for a computer research class in my senior year of high school, but it was also where I first developed my passion for natural language processing and the power of generative AI. I've come a *long* way since then, but I hope you enjoy what you find here!

Warning: I can't promise that none of this has been deprecated (and knowing 17 year-old me, files *may* be missing)

## How to speak to Chatthew (Chatt for short)

All of the functionality you need is found within the chatthew.py file :)

## How Chat works

Speech to text: The SpeechRecognition library utilizes the user's microphone and gets their input, stopping if they say "quit" or "goodbye," or if they pause for long enough.

Response generation: I use PyTorch to tokenize the text, employing a Bag-of-Words model that then randomly selects from a list of responses with a high enough confidence value.

Text to speech: pyttsx3 handles the speech output, using a pre-installed Siri voice option.
