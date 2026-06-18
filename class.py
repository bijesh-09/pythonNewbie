from car import Car

car1 = Car("BMW", 2020, "Black", True)
print(Car.num_of_cars)
car2 = Car("Audi", 2019, "White", False)
print(Car.num_of_cars)
car3 = Car("Mercedes", 2021, "Silver", True)
print(Car.num_of_cars)

car1.showCar()
car2.showCar()
car3.showCar()

print(car1.isCar)
print(Car.isCar)