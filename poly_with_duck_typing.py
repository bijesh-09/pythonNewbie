class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

class Car:
    # is_alive = False
    def drive(self):
        return "Vroom!"
    
animals = [Dog(), Cat(), Car()]
for animal in animals:
    if isinstance(animal, Animal):
        print(animal.speak())
    else:
        print(animal.drive())
    # print(animal.is_alive)