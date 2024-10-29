class Animal():
    alive = True
    fed = False

    def __init__(self,name):
        self.name = name

class Plant():
    adible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        self.food = food



class Predator(Animal):

class Flower(Plant):

class Fruit(Plant):
    edible = True

if __name__ == '__main__':
