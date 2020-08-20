import random
n = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")


for x in range(5, -1, -1):
    q = int(input("\nWhat's the number? "))
    if q == n:
        print("Yes! You win!")
        break
    elif q > 10:
        print("Oops, it has to be a number between 1 and 10.")
        
    elif q < n:
        print(f"{q} is too low.")
        
    elif q > n:
        print(f"{q} is too high.")
        
    elif x == -1:
        print("You ran out of guesses!")
    
    print(f"You have {x} guesses left")