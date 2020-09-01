#Task: Write a program that asks the user for a numerical input, 'n', and prints out the next 'n' numbers of the fibonacci sequence. ( 1 , 1 , 2 , 3, 5, 8, 1 3, 2 1 , 34. . . )

user_input = int(input("How many Fibonacci numbers would you like to see? "))

count = 0
before = 0
next = 1
sum = 1

while count <= user_input:
    print(f"{before} ->", end=" ")
    count = count + 1
    sum = next + before
    before = next
    next = sum

print("END", end=" ")


