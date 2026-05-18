name = "bro"
print(f"Hello {name}!") 
is_student = False
if is_student:
    print("You are a student.")
elif not is_student:
    pass
    print("You are not a student.")
else:
    print("You are not a student.")

age = 20
age = str(age)
print(type(age))
# total_age = age + 1   
# print(total_age) str + int , cant concatenate error
real_total_age = age + "1"
print(real_total_age) # 201

something = None
print(bool(something))

# l = float(input("Enter length: "))
# b = float(input("Enter breadth: "))
# area = l * b
# print(f"The area of the rectangle is: {area}cm²") # cm² the 2 here is a superscript, alt + 0178 

import math
print(math.pi)
print(math.e)
x = 2
print(math.sqrt(x))
y = -2.9
print(math.ceil(y))
print(math.floor(y))
y = 2.9
print(math.ceil(y))
print(math.floor(y))

r = 5
c = 2 * math.pi * r
print(f"The circumference of the circle is: {round(c,5)}cm")

# return - gives value and STOPS
def my_func():
    return 10
    return 2  # Never reached
    
print(my_func())  # 1

# yield - gives value and PAUSES
def my_generator():
    yield 1
    yield 2
    yield 3
    
# gen = my_generator()
# print(gen) #<generator object my_generator at 0x000001DC2DF95A60>
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# print(next(gen))  # Error: StopIteration

# print("wassup")

#the fresh my_generator would be created here but the program has already crashed due to Error: StopIteration so code below the stopped point wont execute
for num in my_generator():
    print(num)  # 1, then 2, then 3, no error

a=10
b=2
num = a if a > b else b
print(num) 

# print(help(int))

# username = input("Enter your username: ")

# print(len(username))
# print(username.find("o") ) #find 1st occurrence of "o" and return index, if not found returns -1
# print(username.rfind("o") ) #find last occurrence of "o" and return index, if not found returns -1
# print(username.count("o") ) #count number of occurrences of "o"
# print(username.capitalize()) #capitalizes the first letter of the string and makes the rest lowercase
# print(username.upper())
# print(username.lower())
# print(username.title()) #capitalizes the first letter of each word and makes the rest lowercase
# print(username.isdigit()) #returns True if all characters in the string (returned by input() normally) are digits(cannot be spaces or special characters or alphabets), otherwise returns False
# # eg username = "123" from input() then isdigit() returns True, so it must be string with digits only
# print(username.isalpha()) #returns True if all characters in the string are alphabetic (cannot be spaces or special characters or numbers), otherwise returns False

# phone_number = input("Enter your phone number: ")
# print(phone_number.replace(" ", "-")) #1 2 34 567 => 1-2-34-567

credit_number = "1234-5678-9012-3456"
print(credit_number[0:4]) #1234
print(credit_number[:4]) #1234
print(credit_number[5:9]) #5678, 5 is included but 9 is not included
print(credit_number[5:]) #5678-9012-3456, 5 is included but since there is no end index, it goes till the end of the string
print(credit_number[-4:]) #last 4 digits
print(credit_number[::-1]) #reverses the string
print(credit_number[::3]) #takes every 3rd character from the string

price = 30000000000000.14159
print(f"{price:.2f} dollars.") 
print(f"{price:10} dollars.") 
print(f"{price:010} dollars.") 
print(f"{price:>10} dollars.") 
print(f"{price:<10} dollars.") 
print(f"{price:>010} dollars.") 
print(f"{price:<010} dollars.") 
print(f"{price:^010} dollars.") 
print(f"{price:^10} dollars.") 
print(f"{price:+} dollars.") 
print(f"{price: } dollars.") 
print(f"{price:,} dollars.") 

for x in reversed(range(1,11,2)):
    print(x)
print("----")
for x in range(5):
    print(x)

# import time
# time.sleep(2)
# print("Hello after 2 seconds!")

lists = [1, 2, 3, 4, 5]
print(lists[:3])
for item in lists:
    print(item)
print(dir(lists)) 
# print(help(list)) 
print(list(lists))
print(1 in lists) 
lists[0] = 10
print(lists)
lists.append(10)
print(lists)
lists.insert(0, "apple")
print(lists)
# lists.sort() 
print(lists)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
combined_list = list1 + list2 + list3
twoD_list = [list1, list2, list3]
print(combined_list)
print(twoD_list)
for sublist in twoD_list:
    for item in sublist:
        print(item, end=" ")
print() 
print(twoD_list[0])
print(twoD_list[0][1])

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for key in row:
        print(key, end=" ")
    print()

dict = {1:"hi", 2:"hello", 3:"wassup"}
print(dict)
for key in dict.keys():
    print(key)
for value in dict.values():
    print(value)
for key, value in dict.items(): #returns 2d list of tuples of keyvalue pair
    print(f"{key}: {value}")
dict.pop(2)
print(dict)
print(dict.get(3))
print(dict.get(4))

import time
def count(start, end):
    for i in range(start, end+1):
        print(i)
        time.sleep(1)

# count(1, 5)

def hello(greetings,title,  first_name, last_name):
    print(f"{greetings} {title} {first_name} {last_name}!")

hello("Hello", first_name="John", title="Mr.", last_name="Doe")

def add(*args):
    total = 0
    for arg in args:
        total+=arg
    return total
print(add(1,2,3,4,5,6,7,8,9))

def addr(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    if "apt" in kwargs:
        print("Apt number is present in the address.")
    for key in kwargs:
        print(key, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    # print()

addr("Hello", "World", name="John", age=30, city="New York", apt=101)

numbers_list = ( 2, 1, 3, 4, -3, 5, -1, -2)

for num in reversed(numbers_list):
    print(num, end=" ")
print()
pos_nums = [num for num in numbers_list if num >=0]
print(pos_nums)
neg_nums = [num for num in numbers_list if num < 0]
print(neg_nums)


# grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# student = input("Enter student name: ").capitalize()
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print("Student not found.")

doubles = [x*2 for x in range(1, 11)]
print(doubles)

fruits = [fruit.upper() for fruit in ["apple", "banana", "cherry"]]
print(fruits)
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

# vowel = input("Enter a vowel: ").lower()

# def is_vowel(char):
#     match char:
#         case "a" | "e" | "i" | "o" | "u":
#             return True
#         case _:
#             return False

# if is_vowel(vowel):
#     print(f"{vowel} is a vowel.")
# else:
#     print(f"{vowel} is not a vowel.")

# import math as m
# print(m.sqrt(16))

# # from math import  pi, e 
# a, b , e = 1, 2, 3
# print(m.pi)
# print(m.e ** a)
# print(m.e ** b)