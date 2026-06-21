import random

words = ("apple", "banana", "orange", "pineapple", "coconut")

hangman_art = {0: ("   ",
                   "   ",
                   "   ",),
               1: (" o ",
                   "   ",
                   "   ",),
               2: (" o ",
                   " | ",
                   "   ",),
               3: (" o ",
                   "/| ",
                   "  ",),
               4: (" o ",
                   "/|\\",
                   "   ",),
               5: (" o ",
                   "/|\\",
                   "/  ",),
               6: (" o ",
                   "/|\\",
                   "/ \\",)}

# for i in hangman_art:
#     print("\n".join(hangman_art[i]))
#     # for j in range(len(hangman_art[i])):
#     #     print(hangman_art[i][j])

# dict = {1: ("wassup", "boy"), 2: ("i am", "home")}
# print(dict[1])
# print(dict[2])
# for i in dict:
#     print(" ".join(dict[i]))
#     # print(dict[i][0], dict[i][1])

def display_man(wrong_guesses):
    print("-"*15)
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("-"*15)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    play_again = True

    while play_again:
        ans = random.choice(words)
        hint = ["_"] * len(ans)
        wrong_guesses = 0
        guessed_letters = set()
        is_running = True
        guess_num = 0
        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)

            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue
            
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}. Try again.")
                continue

            guessed_letters.add(guess)
            guess_num += 1

            if guess in ans:
                for i in range(len(ans)):
                    if ans[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1

            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(ans)
                print(f"Congratulations! You've guessed the word in {guess_num} guesses!")
                is_running = False
                
            elif wrong_guesses >= len(hangman_art) - 1:
                display_man(wrong_guesses)
                print(f"Game Over! You've been hanged! The word was:")
                display_answer(ans)
                is_running = False
                
        play_again_input = input("Do you want to play again? (y/n): ").lower()
        if play_again_input == 'y':
            play_again = True
        else:
            play_again = False
        
if __name__ == '__main__':
    main() 

