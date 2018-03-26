# contributors ayla parsons, hamid tavakoli
# This is a console text based game.
# the concept is still under development
import random
import player
import dice
import enemies
import food
import weapons

endingDictionary = {
                    "LLLLL": """You are in Hell, and your roommate is
                    The Night King""",
                    "LLLLR": """You are in Heaven, and your roommate is
                    Jon Snow, King in the North""",
                    "LLLRL": """You are in Heaven, and your roommate is
                    Carol Ranz""",
                    "LLLRR": "You are in Hell, and your roommate is Tim",
                    "LLRLL": """You are in Hell, and your roommate is
                    Andrew Leslie""",
                    "LLRLR": """You are in Heaven, and your roommate is
                    Matt LeBlanc""",
                    "LLRRL": """You are in Hell, and your roommate is
                    Professor James Moriarty""",
                    "LLRRR": """You are in Heaven, and your roommate is
                    Detective Sherlock Holmes""",
                    "LRLLL": """You are in Heaven, and your roommate is
                    Professor Severus Snape""",
                    "LRLLR": """You are in Heaven, and your roommate is
                    Harry Potter""",
                    "LRLRL": """You are in Hell, and your roommate is
                    a Dementor""",
                    "LRLRR": """You are in Hell, and your roommate is
                    Lord Voldemort""",
                    "LRRLL": """You are in Heaven, and your roommate is
                    Batman""",
                    "LRRLR": """You are in Hell, and your roommate is
                    The Joker""",
                    "LRRRL": """You are in Heaven, and your roommate is
                    Wonder Woman""",
                    "LRRRR": """You are in Hell, and your roommate is
                    Lex Luthor""",
                    "RLLLL": """You are in Hell, and your roommate is
                    Stannis Baratheon""",
                    "RLLLR": """You are in Heaven, and your roommate is
                    Ned Stark""",
                    "RLLRL": """You are in Heaven, and your roommate is
                    Princess Leia""",
                    "RLLRR": """You are in Hell, and your roommate is
                    Joffrey Baratheon""",
                    "RLRLL": """You are in Hell, and your roommate is
                    Darth Vader""",
                    "RLRLR": """You are in Heaven, and your roommate is
                    Han Solo""",
                    "RLRRL": """You are in Heaven, and your roommate is
                    Gandalf""",
                    "RLRRR": """You are in Hell, and your roommate is
                    Saruman""",
                    "RRLLL": """You are in Heaven, and your roommate is
                    Yennefer of Vengerberg""",
                    "RRLLR": """You are in Hell, and your roommate is
                    Emhyr var Emreis""",
                    "RRLRL": """You are in Hell, and your roommate is
                    Radovid the Stern""",
                    "RRLRR": """You are in Heaven, and your roommate is
                    Emiel Regis Rohellec Terzeif Godefroy""",
                    "RRRLL": """You are in Heaven, and your roommate is
                    Hermione Granger""",
                    "RRRLR": """You are in Hell, and your roommate is
                    Dolores Umbridge""",
                    "RRRRL": """You are in Hell, and your roommate is
                    Bellatrix Lestrange""",
                    "RRRRR": """You are in Heaven, and your roommate
                    is Fred Weasley"""
                    }

isFinished = False
decisionsString = ""


def greetUser():
    print('Welcome\nHere you will walk the path of your destiny.')


def showTutorial():
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


def startGame():
    global isFinished
    gamePlayer = player.Player()
    gameDice = dice.Dice()
    getRoomDecision()
    while(not isFinished):
        rollNumber = gameDice.roll()
        gameObject = getGameObject(number=rollNumber)
        if gameObject is None:
            if len(decisionsString) == 5:
                endGame()
                break
            elif len(decisionsString) < 5:
                getRoomDecision()
            else:
                break
        elif isinstance(gameObject, enemies.Enemy):
            print("""Destiny has put a {} in your path.
                Good luck!""".format(gameObject.name))
            remainingHealth = gamePlayer.fight(enemy=gameObject)
            if remainingHealth <= 0:
                print("""You got seriously damaged during your fight with the
                    {}""".format(gameObject.name))
                dealWithDeath()
            else:
                print("""After the fight your health is
                    at {}""".format(remainingHealth))
                # give them a chance to eat foodToEat
                toEatOrNotToEat = input("""Would you like to
                    eat some food to regenerate health?(Y,N)""").upper()
                if toEatOrNotToEat == 'Y':
                    gamePlayer.eat()
        elif isinstance(gameObject, weapons.Weapon):
            weaponChoice = input("""There is a {} here, would you
                like to pick it up?(Y,N)""".format(gameObject.name)).upper()
            if weaponChoice == 'Y':
                gamePlayer.pickUpWeapon(weapon=gameObject)
        elif isinstance(gameObject, food.Food):
            foodChoice = input("""There is a {} here, would you
                like to pick it up?(Y,N)""".format(gameObject.name)).upper()
            if foodChoice == 'Y':
                gamePlayer.pickUpFood(food=gameObject)
        else:
            break


def getRoomDecision():
    decision = input("""Destiny has put two paths before you. A room to your
        left and a room to your right. Which one do you want to
        take?(L,R)""").upper()
    if decision == "R" or decision == "L":
        global decisionsString
        decisionsString += decision
    else:
        getRoomDecision()


def endGame():
    global decisionsString
    ending = endingDictionary[decisionsString]
    print(ending)


def dealWithDeath():
    grimReaper = GrimReaper()
    toBegOrNotToBeg = input("""You are about to die. The Grim Reaper is here.\n
        Would you like to beg for another chance?(Y,N)""").upper()
    if toBegOrNotToBeg == 'Y':
        grimReaper.play()
    else:
        global isFinished
        isFinished = True
        GrimReaper.takeLife()


def getGameObject(number):
    """ 1 <= number <= 6"""
    randomNum = random.randint(1, 3)
    if number == 1 or number == 6:
        # we should get an enemy
        enemyFactory = enemies.EnemyFactory()
        return enemyFactory.getEnemy(code=randomNum)
    elif number == 2:
        # we should retrun a food
        foodFactory = food.FoodFactory()
        return foodFactory.getFood(code=randomNum)
    elif number == 3 or number == 5:
        # we should return a weapon
        weaponFactory = weapons.WeaponFactory()
        return weaponFactory.getWeapon(code=randomNum)
    else:
        # we should return a room
        return None


class GrimReaper():
    def takeLife():
        print("""Grim Reaper:You failed.You are doomed to
            burn in hell for eternity.""")
        global isFinished
        isFinished = True

    def letUserContinue():
        print('Grim Reaper:You got lucky this time. We will meet again!')

    def play(self):
        randomNumber = random.randint(1, 2)
        print("""I have picked a number between 1 and 2. If you guess it,
            I will give you another chance.""")
        enteredNumber = int(input('What is your guess?'))
        if randomNumber == enteredNumber:
            # let the user continue
            GrimReaper.letUserContinue()
        else:
            GrimReaper.takeLife()


def main():
    """The game logic"""
    greetUser()
    showTutorial()
    startGame()


if __name__ == '__main__':
    main()
