class Enemy():

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    # def attack(self, player):
    #     playerPower = player.getPower()
    #     if playerPower >= self.strength:
    #         player.takeDamage(self.strength)
    #     else:
    #         player.die()


class Gohst(Enemy):
    def __init__(self):
        super.__init__(self, 'Gohst', 30)


class ThreeHeadedDog(Enemy):
    def __init__(self):
        super.__init__(self, 'ThreeHeadedDog', 130)


class DarkShadow(Enemy):
    def __init__(self):
        super.__init__(self, 'ThreeHeadedDog', 90)


class EnemyFactory():

    def getEnemy(code):
        if code == 1:
            return Gohst()
        elif code == 2:
            return ThreeHeadedDog()
        elif code == 3:
            return DarkShadow()
        else:
            print('{} is not a valid enemy code.'.fomrat(code))
