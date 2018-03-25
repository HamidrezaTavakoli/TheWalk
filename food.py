class Food():
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Fruit(Food):
    def __init__(self):
        super().__init__('fruit', 45)


class Meat(Food):
    def __init__(self):
        super().__init__('meat', 75)


class Water(Food):
    def __init__(self):
        super().__init__('water', 55)


class FoodFactory():

    def getFood(self, code):
        if code == 1:
            return Fruit()
        elif code == 2:
            return Meat()
        elif code == 3:
            return Water()
        else:
            print('{} is not a valid food code.'.fomrat(code))
