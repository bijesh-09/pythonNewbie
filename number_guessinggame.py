import random

low = 1
high = 100

ans = random.randint(low, high)

guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"Select a number between {low} and {high}.")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print(f"Please select a number between {low} and {high}.")
        elif guess < ans:
            print("Too low! Try again.")
        elif guess > ans:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You've guessed the number {ans} in {guesses} guesses.")
            is_running = False
    else:
        print("Invalid input. Please enter a number.")
