def madlib(name, subject):
    return f"{name}'s favorite subject is {subject}."


name = str(input("What's your name?\n>"))
subject = str(input("What's your favorite subject?\n>"))
message = madlib(name, subject)
print(message)