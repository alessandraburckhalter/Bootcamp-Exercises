print("I am thinking of a number between 1 and 10.")

while True:
    q = int(input("What's the number? "))
    if q == 5:
        print("Yes! You win!")
    elif q > 10:
        print("Ooops, it has to be a number between 1 and 10.")
    elif q < 5:
        print(f"{q} is too low.")
    elif q > 5:
        print(f"{q} is too high.")