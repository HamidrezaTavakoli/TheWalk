class Weapon():
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Sword(Weapon):
    def __init__(self):
        super().__init__('Sword', 50)


class MagicWand(Weapon):
    def __init__(self):
        super().__init__('MagicWand', 80)


class ThorsHammer(Weapon):
    def __init__(self):
        super().__init__('ThorsHammer', 120)


class WeaponFactory():
    def getWeapon(self, code):
        if code == 1:
            return Sword()
        elif code == 2:
            return MagicWand()
        elif code == 3:
            return ThorsHammer()
        else:
            print('{} is not a valid weapon code'.format(code))
