# ask user to input a positive number
user_input = int(input("Hi there. Please, enter a positive number: "))

# print numbers from 1 to user's input number
for num in range(1, user_input + 1): # "+ 1" to get the user's input number printed
# find if numbers in range are divisible by 3 and 5, if so, print "fizzbuzz" instead of the numbers
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
# find if numbers in range are divisible by 3, if so, print "fizz" instead of the numbers
    elif num % 3 == 0:
        print("fizz")
# find if numbers in range are divisible by 5, if so, print "buzz" instead of the numbers
    elif num % 5 == 0:
        print("buzz")
# if numbers in range are not divible by 3 or/and 5, print the numbers
    else:
        print(num)