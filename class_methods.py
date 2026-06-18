class Student:
    count = 0
    total_age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
        Student.total_age += age

    # instance method
    def say_hi(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod 
    def get_avg_age(cls):
        if cls.count == 0:
            return 0
        return cls.total_age / cls.count

    
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
print(Student.get_count())
print(Student.get_avg_age())