class Car:
    isCar = True
    num_of_cars = 0
    def __init__(self, modal, year, color, for_sale):
        Car.num_of_cars += 1
        self.modal = modal
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def showCar(self):
        print(f"Modal: {self.modal}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"For Sale: {self.for_sale}")
        print()
    
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Fish(Prey, Predator):
    def __init__(self, name):
        self.name = name

fish = Fish("Nemo")
fish.eat()
fish.sleep()
fish.flee()
fish.hunt()