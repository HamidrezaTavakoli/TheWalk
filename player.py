class Player():

    def __init__(self):
        self.health = 100.0
        self.food = list()
        self.weapons = list()

    def eat(self):
        if len(self.food) > 0:
            foodToEat = self.food.pop()
            if self.health < 100.0:
                self.health = max((self.health + foodToEat.power), 100)
            else:
                self.health = 100.0
        else:
            print('No food to eat at the moment')

    def pickUpFood(self, food):
        if len(self.food) < 2:
            self.food.append(food)
        else:
            print('Your pockets are already full')

    def pickUpWeapon(self, weapon):
        if len(self.weapons) < 2:
            self.weapons.append(weapon)
        else:
            print('You can not carry more than 2 weapons')

    def fight(self, enemy):
        enemyPower = enemy.strength
        lastWeapon = self.weapons.pop()
        self.health = (self.health + lastWeapon.power) - enemyPower
        return self.health
