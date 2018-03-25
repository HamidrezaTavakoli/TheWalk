class Player():

    def __init__(self):
        self.health = 100.0
        self.food = list()
        self.weapons = list()

    def eat(self):
        if len(self.food) > 0:
            foodToEat = self.food.pop()
            self.health = min((self.health + foodToEat.power), 100)
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
        if len(self.weapons) > 0:
            lastWeapon = self.weapons.pop()
            self.health = min((self.health + lastWeapon.power) - enemyPower, 100)
        else:
            self.health = self.health - enemyPower
        return self.health
