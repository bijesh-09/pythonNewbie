# random_name = "example_name"
# multiple_names = """name1 name2
#  name3
#  name4"""
# print(random_name)
# print(multiple_names)

# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[:3])
# print(course[3:])
# print(course[:])
# print(course[0:])

# # print each character in reverse on the same line.
# # Use a range that covers the whole string with negative indices:
# for i in range(-1, -len(course)-1, -1):
#     print(course[i], end='')
# print()  # newline after the loop
# for i in range(0, len(course), +1):
#     print(course[i], end='')
# print()

# # Alternative, more idiomatic ways to print reversed on one line:
# for ch in reversed(course):
#     print(ch, end='')
# print()
# # or simply:
# print(course[::-1])

# course_name = "Python \"Programming"
# print(course_name)
# course_name = "Python \'Programming"
# print(course_name)
# course_name = "Python \/Programming"
# print(course_name)
# course_name = "Python \\Programming"
# print(course_name)
# course_name = "Python \nProgramming"
# print(course_name)

# first = "ram"
# last = "kumar"
# full = first + " " + last #concatenation
# print(full)
# fullname = F"{first} {last}" #formatted string
# # fullname = f"{first} {last}" use F"" or f"" for fromatted string
# print(fullname)
# var = f"{len(first) } {2+3}"
# print(var)

# course = "    Python Programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.find("pro"))
# print(course.replace("Pro", "Language"))
# print("Programming" in course)
# print("programming" in course)
# print("Programming" not in course)

# print(10//3)
# print(13**2)
# print(round(2.675, 2))
# print(round(2.675))
# print(abs(round(-2.675)))

# x = input("Enter x: " )
# print(type(x))
# y= int(x) + 5
# print(f"x: {x}, y: {y}")

# print(bool(" "))
# print(bool("False"))
# print(bool(""))
# print(bool(0))
# print(bool(None))
# print(bool(1))
# print(bool(-1))


# fruit = "apple"
# print(fruit[1:-1])
# print(fruit[1:])
# course = "Python Programming"
# print(course[3:])
# print(course[1:-1])

# print(ord("b") < ord("a"))
# print(ord("B") - ord("b"))

# temp = 20

# if temp>30:
#     print("Hot day")
#     print("Drink water")
# print("Enjoy your day")

# age=19;
# msg= "Eligible" if age>=18 else "Not Eligible"
# print(msg)
# success = 0
# for i in range(3):
#     if success:
#         print("Success")
#         break
# else: print("Failed")

# for i in [1,2,3,4,5]:
#     print(i, end=' ')
# print(type([] ) )

# cmd = ""
# while cmd.upper() != "QUIT":
#     cmd = input()
#     print("ECHO", cmd)

# def greet(name):
#     return "Hello " + name
# # file = open("greet.txt", "w")
# # file.write(greet("Alice"))
# # file.close()
# print(greet("Alice"))

# def increment(number, by=1):
#     return number + by
# print(increment(5, y=2))

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     print(total)
# multiply(2,3,4)

# t = (1,2,3)
# print(*t)

# fruits = ["apple", "banana", "cherry"]
# print(dir(fruits))
# print(help(fruits))

# list
# fruits = ["apple", "banana", "orange", "coconut"]

# fruits.append("mango")
# fruits.insert(1, "grape")
# fruits[0] = "kiwi"
# fruits.remove("banana")
# print(fruits.pop())
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("orange"))
# print(fruits.count("apple"))

# print(fruits)

# fruits = ("apple", "banana", "orange", "coconut", "apple")
# fruits.add("mango")
# fruits.remove("mango")
# fruits.clear()

# print(fruits )
# for fruit in fruits:
# print(fruit)

# capitals = {"USA": "Washington DC",
            # "India": "New Delhi", "Nepal": "Kathmandu"}
# print(dir(capitals))
# print(help(capitals))
# capitals.update({"UK": "London"})
# capitals["USA"] = "Washington"
# capitals.update({"India": "Bihar", "USA": "New York"})
# i , j = capitals.popitem()
# print(f"Removed: {i} → {j}")
# print(capitals.pop("USA"))
# print(capitals.popitem())

# print (capitals.keys()) 
# print (capitals.values())
# for i,j in capitals.items():
    # print(f"{i} : {j}")
# print (capitals.items())

# print(capitals)
