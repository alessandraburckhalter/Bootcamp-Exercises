#Task: Implement try and except to the code

print("\nLet's play a game!")
print("\nI'm thinking of a number between 1 and 10.")

while True:
    try:
        question = int(input("\nWhat's the number? "))
        if question == 5:
            print("Yes! You win!")
        elif question > 10:
            print("Oops, it has to be a number between 1 and 10.")
        elif question < 5:
            print(f"{q} is too low.")
        elif question > 5:
            print(f"{question} is too high.")
            break
        
    except ValueError:
        print('Please try again.')

