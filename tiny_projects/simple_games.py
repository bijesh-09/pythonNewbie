# quiz game
qns = (
    "How many elements are there in the periodic table? ",
    "Which animal lays the largest eggs? ",
    "What is the most abundant gas in the Earth's atmosphere? ",
    "How many bones are there in the human body? ",
    "Which planet in the solar system is the hottest? "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter")
)

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
qn_num = 0

for qn in qns:
    print("-----------------------------")
    print(qn)
    for option in options[qn_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[qn_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    qn_num +=1

print("Correct answer:")
for ans in answers:
    print(ans, end=" ")
print()
print("Your guess:")
for guess in guesses:
    print(guess, end=" ")
print()
print(f"Your score: {score}")
print(f"Score%: {score/len(qns)*100:.2f}%")
