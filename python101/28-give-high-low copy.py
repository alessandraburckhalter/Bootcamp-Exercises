print("\nLet's play a game!")
print("\nI'm thinking of a number between 1 and 10.")

while True:
    try:
        q = int(input("\nWhat's the number? "))
        if q == 5:
            print("Yes! You win!")
        elif q > 10:
            print("Oops, it has to be a number between 1 and 10.")
        elif q < 5:
            print(f"{q} is too low.")
        elif q > 5:
            print(f"{q} is too high.")
            break
        
    except ValueError:
        print('Please try again.')

