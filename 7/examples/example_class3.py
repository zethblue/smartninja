class Snake(object):
    def __init__(self,name):
        self.name = name
        self.food = []

    def eat(self,newfood):
        self.food.append(newfood)

if __name__ == '__main__':
    franz = Snake("Franz")
    print franz.name
    print franz.food
    franz.eat("Apfel")
    print franz.food
    franz.eat("Maus")
    print franz.food

    A= raw_input("What shall Franz eat?")
    franz.eat(A)
    print franz.food