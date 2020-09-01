#Task: Prompt the user for his name using the input function. Print the user's name in ALL CAPS, and also tell them the number of letters in their name.

name = input("What's your name? ".upper())
greeting = f"Hello, {name}!"
letters = len(name)
print(greeting.upper())
print(f"Your name has {letters} letters in it! Awesome".upper())



