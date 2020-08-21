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


