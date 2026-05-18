from script1 import *

def fav_drink(drink):
    print(f"My favorite drink is {drink}")

def main():
    print("this is script2")
    fav_drink("coffee")
    fav_food("sushi")
    print(" | ".join([str(x+1) for x in range(5)]))

if __name__ == '__main__':
    main()