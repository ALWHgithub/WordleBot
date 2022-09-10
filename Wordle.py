
from asyncio.windows_events import NULL
import math
from nltk.corpus import brown
from nltk.corpus import words
from random import random


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
master_word_list = [x for x in brown.words() if (
    len(x) == 5 and x[0] in letters and x[1] in letters and x[2] in letters and x[3] in letters and x[4] in letters)]

global correctWord
correctWord = master_word_list[math.floor(random()*len(master_word_list))]

global correctPostion
correctPostion = ["*", "*", "*", "*", "*"]

global prev
prev = ""


def handleReply(msg):
    global correctPostion
    global correctWord
    global prev
    if (msg == correctWord):
        correctWord = master_word_list[math.floor(
            random()*len(master_word_list))]
        correctPostion = ["*", "*", "*", "*", "*"]
        prev = ""
        return "Nice One!"
    elif (msg == None or len(msg) != 5 or msg not in master_word_list):
        return "invalid guess"
    else:
        print(correctWord)
        positionString = ""
        correctLetters = ""
        for x in range(0, 5):
            if correctWord[x] in msg:
                correctLetters += correctWord[x] + ", "
            if msg[x] == correctWord[x]:
                correctPostion[x] = msg[x]
            positionString += correctPostion[x]
        final_msg = msg + ": " + positionString + \
            " <b>Correct Letters</b> " + correctLetters
        prev += final_msg + "\n"
        return prev
