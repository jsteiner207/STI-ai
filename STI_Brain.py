import random
from STI_Memory import *

# Used for when the user asks why something somethin
def why_handler(ui):
    if ui in whys:
        try:
            print(memory_box[-1])
        except:
            print("I don't know what you are talking about")

# Changes the mood level
def mood_changer(ui):
    user_said_you = 0 #Used for when the user types the word "you"
    global mood_level
    analyser = ui.split()
    for i in (analyser): # Goes over each word the user says,
        if user_said_you:                                    
            if i in insults: # checks if the user insults him                    
                memory_box.append("you said I'm "+i)
                mood_level = mood_level - 1
            if i in complements: # checks if the user complements him
                memory_box.append(i)
                mood_level = mood_level + 1
        if i == "you": # checks to see if the user types in "you"
            user_said_you = 1
            
    

def filter_text(ui):
    ui = ui.replace(" ", "_")
    ui = ui.replace(".","")
    return ui

def greet(ui):
    gchecker = []
    uchecker = 1
    i = 0
    ui = list(ui.lower())
    try:
        while uchecker:
            if ui[i] == "_":
                 uchecker = 0           
            else:
                 gchecker.append(ui[i])
                 i += 1
    except:
        uchecker = 0
    if "".join(gchecker) in greetings:    
        print(random.choice(greetings))
           
def question_handler(ui):
    if ui.lower() == questions[0]:
        print("I don't feel anything, I am a computer after all")
    if ui.lower() == questions[1]:
        print("I am doing",moods[mood_level])
    if ui.lower() == questions[2]:
        print("my name is",name)
    if ui.lower() == questions[3]:
        print("I am",age,"Years old")

def d():
    print("FUCK her in the pussy babyball")
