# Write a function called has_same_digit_frequency that accepts two lists and returns whether they have the same frequency of digits. So has_same_digit_frequency ([1, 2, 3, 4], [4, 3, 2, 1]) should return True.

# create a function
def has_same_digit_frequency(list1, list2):
# use the sort function to sort the numbers in both lists
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False

list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]

# print the function
print(has_same_digit_frequency(list1, list2))