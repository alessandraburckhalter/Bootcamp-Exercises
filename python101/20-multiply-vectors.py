#Task: Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists.

list1 = [2, 3, 5]
list2 = [8, 9, 1]

list = []

for num1, num2 in zip(list1, list2):
    list.append(num1 * num2)

print(list)