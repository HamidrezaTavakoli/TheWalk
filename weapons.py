class Weapon():
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Sword(Weapon):
    def __init__(self):
        super.__init__(self, 'Sword', 30)


class MagicWand(Weapon):
    def __init__(self):
        super.__init__(self, 'MagicWand', 50)


class WarHammer(Weapon):
    def __init__(self):
        super.__init__(self, 'WarHammer', 100)


class WeaponFactory():
    def getWeapon(code):
        if code == 1:
            return Sword()
        elif code == 2:
            return MagicWand()
        elif code == 3:
            return WarHammer()
        else:
            print('{} is not a valid weapon code'.format(code))
