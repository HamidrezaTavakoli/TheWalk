class Enemy():

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


class Ghost(Enemy):
    def __init__(self):
        super().__init__('Ghost', 70)


class ThreeHeadedDog(Enemy):
    def __init__(self):
        super().__init__('ThreeHeadedDog', 90)


class DarkShadow(Enemy):
    def __init__(self):
        super().__init__('DarkShadow', 80)


class EnemyFactory():

    def getEnemy(self, code):
        if code == 1:
            return Ghost()
        elif code == 2:
            return ThreeHeadedDog()
        elif code == 3:
            return DarkShadow()
        else:
            print('{} is not a valid enemy code.'.fomrat(code))
