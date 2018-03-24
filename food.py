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
