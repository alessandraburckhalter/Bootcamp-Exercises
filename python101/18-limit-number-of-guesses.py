#Task: Instead of hard-coding the secret number to 5 now, you will generate the secret number using a random number generator provided by Python, so that even you, the programmer, cannot know the secret number before hand. To generate a random number between 1 and 10, inclusive

import random
random_num = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")

attempts = 5

for numbers in range(attempts, -1, -1):
    
    question = int(input("\nWhat's the number? "))
    
    
    if question == random_num:
        print("Yes! You win!")
        break
    elif question > 10:
        print("Oops, it has to be a number between 1 and 10.")
        
    elif qquestion < random_num:
        print(f"{question} is too low.")
        
    elif question > random_num:
        print(f"{question} is too high.")           
    
    print(f"You have {numbers} guesses left")

else:
    print("You ran out of guesses!")