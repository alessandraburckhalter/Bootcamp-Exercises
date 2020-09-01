#Task: Improve your game to provide the player with a high-or-low hint. 

print("I am thinking of a number between 1 and 10.")

while True:
    question = int(input("What's the number? "))
    if question == 5:
        print("Yes! You win!")
    elif question > 10:
        print("Ooops, it has to be a number between 1 and 10.")
    elif question < 5:
        print(f"{question} is too low.")
    elif question > 5:
        print(f"{question} is too high.")