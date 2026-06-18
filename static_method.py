class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} works as a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Engineer", "Scientist", "Manager"]
        return position in valid_positions


employee1 = Employee("Alice", "Software Engineer")
employee1.is_valid_position = lambda x: False
print(employee1.get_info())
print(employee1.is_valid_position("Engineer"))
print(Employee.is_valid_position("Engineer"))
print(Employee.is_valid_position) #just a ref to fn, not actually calling it. <function Employee.is_valid_position at 0x7f8c8c8c8c8c>