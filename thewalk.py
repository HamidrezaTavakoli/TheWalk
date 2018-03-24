# contributors ayla parsons, hamid tavakoli
# This is a console text based game.
# the concept is still under development
import random

endingDictionary = {"LLLLL":"You are in Hell, and your roommate is The Night King",
    "LLLLR":"You are in Heaven, and your roommate is Jon Snow, King in the North",
    "LLLRL":"You are in Heaven, and your roommate is Carol Ranz",
    "LLLRR":"You are in Hell, and your roommate is Tim",
    "LLRLL":"You are in Hell, and your roommate is Andrew Leslie",
    "LLRLR":"You are in Heaven, and your roommate is Matt LeBlanc",
    "LLRRL":"You are in Hell, and your roommate is Professor James Moriarty",
    "LLRRR":"You are in Heaven, and your roommate is Detective Sherlock Holmes",
    "LRLLL":"You are in Heaven, and your roommate is Professor Severus Snape",
    "LRLLR":"You are in Heaven, and your roommate is Harry Potter",
    "LRLRL":"You are in Hell, and your roommate is a Dementor",
    "LRLRR":"You are in Hell, and your roommate is Lord Voldemort",
    "LRRLL":"You are in Heaven, and your roommate is Batman",
    "LRRLR":"You are in Hell, and your roommate is The Joker",
    "LRRRL":"You are in Heaven, and your roommate is Wonder Woman",
    "LRRRR":"You are in Hell, and your roommate is Lex Luthor",
    "RLLLL":"You are in Hell, and your roommate is Stannis Baratheon",
    "RLLLR":"You are in Heaven, and your roommate is Ned Stark",
    "RLLRL":"You are in Heaven, and your roommate is Princess Leia",
    "RLLRR":"You are in Hell, and your roommate is Joffrey Baratheon",
    "RLRLL":"You are in Hell, and your roommate is Darth Vader",
    "RLRLR":"You are in Heaven, and your roommate is Han Solo",
    "RLRRL":"You are in Heaven, and your roommate is Gandalf",
    "RLRRR":"You are in Hell, and your roommate is Saruman",
    "RRLLL":"You are in Heaven, and your roommate is Yennefer of Vengerberg",
    "RRLLR":"You are in Hell, and your roommate is Emhyr var Emreis",
    "RRLRL":"You are in Hell, and your roommate is Radovid the Stern",
    "RRLRR":"You are in Heaven, and your roommate is Emiel Regis Rohellec Terzeif Godefroy",
    "RRRLL":"You are in Heaven, and your roommate is Hermione Granger",
    "RRRLR":"You are in Hell, and your roommate is Dolores Umbridge",
    "RRRRL":"You are in Hell, and your roommate is Bellatrix Lestrange",
    "RRRRR":"You are in Heaven, and your roommate is Fred Weasley"}

def greetUser():
    print('welcome\nHere you will walk the path of your destiny.')


def tutorial():
    print('In this game you will roll the dice and move.')
    print('At the end of each move you are presented with a surprise.')
    print('Surprises are, Enemies, Weapons, Food and Rooms.')
    print('Food will regenarate a limited amount of health.')
    print("""Choosing which room you want to step in will determine your
        destiny.""")
    print("""In case of gettng killed in a battle with an enemy
        the Grim Reaper will come for your soul.
        You can beg him for another chance and he might give you one.""")
    print('Good Luck and enjoy playing')


class GrimReaper:
    def takeLife(self):
        print('You failed.You are doomed to burn in hell for eternity.')

    def letUserContinue(self):
        print('You got lucky this time. We will meet again!')

    def play(self):
        randomNumber = random.int(1, 5)
        print("""I have picked a number between 1 and 5. If you guess it,
            I will give you another chance.""")
        enteredNumber = int(input('What is your guess?'))
        if randomNumber == enteredNumber:
            # let the user continue
            GrimReaper.letUserContinue()
        else:
            GrimReaper.takeLife()
