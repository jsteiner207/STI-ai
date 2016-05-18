# STI BOT       #       
# Jacob Steiner #      
# 5/14/2014     #

import random
from STI_Brain import *
from STI_Memory import *

print("Welcome to STI-bot beta, if you would like to stop talking to me, just close the window")

ui = input("")

looper = True
while looper:
   
    mood_changer(ui)
    ui = filter_text(ui)
    why_handler(ui)
    greet(ui)
    question_handler(ui)
    ui = input("")

