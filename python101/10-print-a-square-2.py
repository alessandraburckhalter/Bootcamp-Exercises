#Task: Print a NxN square of * characters. Prompt the user for N. 

n = int(input("How big is the square? "))

for data in range(0, n):
    print(n * "*")