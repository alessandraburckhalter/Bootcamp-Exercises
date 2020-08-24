# Task: Write a function that accepts two arguments: a name and a subject.
# The function should return a String with the name and subject interpolated in.

# create the function
def madlib(name, subject):
    return f"{name}'s favorite subject is {subject}."

# ask user to input name and subject
name = str(input("What's your name?\n> "))
subject = str(input("What's your favorite subject?\n> "))
# print function
print(madlib(name, subject))