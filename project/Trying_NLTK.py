import nltk

from nltk.chat.util import Chat, reflections

set_pairs = [
                [
                    r"hello|hi|hey|what's up", ["Hi, how are you?", "How is it going?"]
                ],
                [
                    r"who are you?|what are you?", ["I am NLTK_Bot", "I am Mr. NLTK_Bot"]
                ]
]


# What if I tried it with my own corpora? Well: (doesn't work)
"""
stuff = open("/Users/joshuaroussak/Desktop/Chatthew/project/CURRENT_DATA/MyTrainer.yml").read().splitlines()

questions = []
for line in stuff:
    if "question: " in line:
        questions.append(line[12:])

answers = []
num_of_lines = -1
for line in stuff:
    num_of_lines+=1
    if "answer: " in line:
        questions.append(stuff[num_of_lines+1][12:])

set_pairs = [questions,answers]
"""

chat = Chat(set_pairs, reflections)

print(chat)

#chat.converse()

if __name__ == "__main__":
    print("yes")
    chat.converse()