# Task: Write a function that accepts a number as an argument and returns a Boolean value. Return True if the number is even; return False if it is not even.

# create the function
def is_even(num):
# If num is even, return true
    if num % 2 == 0:
        return True
    else:
        return False

# Task 2: Write an is_odd function that uses your is_even function to determine if a number is odd. (That is, do not do the calculation - call a function that does the calculation.)
def is_odd(num):
    return not is_even(num)


# ask user to input a number
num_is_even = is_even(int(input("Please, enter an integer number:\n> ")))
# print function
print("This is an even number!: ", num_is_even)


# Task 3: Write a function that accepts a List of numbers as an argument. Return a new List that includes the only the even numbers.
def only_evens(list_of_numbers):
    new_list = []

    for num in list_of_numbers:
    # check if number is even
        if is_even(num):
            # if yes, store in new_list
            new_list.append(num)
    return new_list

numbers_to_check = [11, 20, 42, 97, 23, 10]
print(only_evens(numbers_to_check))



# Taks 4: Write a function that accepts a List of numbers as an argument. Return a new List that includes the only the odd numbers.
def only_odds(list_of_numbers):
    new_list = []

    for num in list_of_numbers:
    # check if number is even
        if num % 2 == 1:
            # if yes, store in new_list
            new_list.append(num)
    return new_list

numbers_to_check = [11, 20, 42, 97, 23, 10]
print(only_odds(numbers_to_check))



