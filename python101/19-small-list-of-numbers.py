print("=-=-=" * 15)
list = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]

print("List = ", list)
print("=-=-=" * 15)

#Task: Create a list of numbers, print their sum.
print("\nSum the numbers")
print(sum(list))
print("=-=-=" * 15)

#Task: Create a list of numbers, print the largest of the numbers.
print("Largest Number")
print(max(list))
print("=-=-=" * 15)

#Task: Create a list of numbers, print the smallest of the numbers.
print("Smallest Number")
print(min(list))
print("=-=-=" * 15)

#Task: Create a list of numbers, print each number in the list that is even.
print("Even Numbers")
for num in list:
    if num % 2 == 0:
        print(num)
print("=-=-=" * 15)

#Task: Create a list of numbers, print each number in the list that is odd.
print("Odd Numbers")
for num in list:
    if num % 2 == 1:
        print(num)
print("=-=-=" * 15)

#task: Create a list of numbers, print each number in the list that is greater than zero.
print("Positive Numbers")
for numb in list:
    if numb > 0:
        print(numb)
print("=-=-=" * 15)

#Task: Create a list of numbers, create a new list which contains every number in the given list which is positive
print("Positive Numbers 2")
newlist = [n for n in list if n > 0]
print(newlist)
print("=-=-=" * 15)

#Task: Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor.
factor = 5
print("Multiply list by ", factor)
multiplied_number = []
for num in list:
    multiplied_number.append(num * factor)
print(multiplied_number)
print("=-=-=" * 15)

#Task: Given a string, print the string reversed.
print("Reverse a string")
string = "Alessandra".upper()
print("String = ", string)
print(string[::-1])