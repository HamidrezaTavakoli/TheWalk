# contributors ayla parsons, hamid tavakoli
# This is a console text based game.
# the concept is still under development
import random


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
    def takeLife():
        print('You failed.You are doomed to burn in hell for eternity.')

    def letUserContinue():
        print('You got lucky this time. We will meet again!')

    def play():
        randomNumber = random.int(1, 5)
        print("""I have picked a number between 1 and 5. If you guess it,
            I will give you another chance.""")
        enteredNumber = int(input('What is your guess?'))
        if randomNumber == enteredNumber:
            # let the user continue
            GrimReaper.letUserContinue()
        else:
            GrimReaper.takeLife()
