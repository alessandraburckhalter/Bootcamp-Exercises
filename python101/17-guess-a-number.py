#Task: You will implement a guess-the-number game where the player has to try guessing a secret number until they gets it right. For now, you will "hard code" the secret number to 5 (just set it to five like secret_number = 5). You will prompt the player to enter a number again and again, each time comparing their input to the secret number. To to that, you will need to write a while loop. If they guess correctly, you will print "You win!", otherwise, you will prompt for a number again.

print("I am thinking of a number between 1 and 10.")

while True:
    question = int(input("What's the number? "))
    if question == 5:
        print("Yes! You win!")
    elif question > 10:
        print("Ooops, it has to be a number between 1 and 10.")
    else:
        print("Nope, try again.")
    