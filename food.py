class Food():
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Fruit(Food):
    def __init__(self):
        super.__init__(self, 'fruit', 30.0)


class Meat(Food):
    def __init__(self):
        super.__init__(self, 'meat', 60)


class Water(Food):
    def __init__(self):
        super.__init__(self, 'water', 40)


class FoodFactory():

    def getFood(code):
        if code == 1:
            return Fruit()
        elif code == 2:
            return Meat()
        elif code == 3:
            return Water()
        else:
            print('{} is not a valid food code.'.fomrat(code))
