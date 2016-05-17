import random
greetings = ["hey", "howdy", "hi", "hello", "hi there"]
questions = ["how_are_you_feeling", "how_are_you", "what_is_your_name", "how_old_are_you", "where_are_you_from", "are_you_a_boy_or_a_girl", "what_up"]

name = "Stewart"
age = 2


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
        print("I don't have emotions, but just for the sake of conversation, I'm doing good")
    if ui.lower() == questions[2]:
        print("my name is",name)
    if ui.lower() == questions[3]:
        print("I am",age,"Years old")

def d():
    print("FUCK her in the pussy babyball")
