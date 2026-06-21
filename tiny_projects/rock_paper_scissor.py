import random

running = True
options = ("rock", "paper", "scissors")

print("Welcome to Rock, Paper, Scissors!")
print("Options: rock, paper, scissors")


while running:

    player = None
    computer = random.choice(options)
    player = input("Enter your choice: ").lower()
    while player not in options:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        player = input("Enter your choice: ").lower()

    if player == computer:
        print("It's a tie!")
    elif ((player == "rock" and computer == "scissors") or
          (player == "paper" and computer == "rock") or
          (player == "scissors" and computer == "paper")):
        print("You win!")
    else:
        print("Computer wins!")

    print(f"player: {player}")
    print(f"computer: {computer}")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        continue
    else:
        print("Thanks for playing!")
        running = False
