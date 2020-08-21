print("=-=-=" * 15)
list = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]

print("List = ", list)
print("=-=-=" * 15)
print("\nSum the numbers")
print(sum(list))
print("=-=-=" * 15)

print("Largest Number")
print(max(list))
print("=-=-=" * 15)

print("Smallest Number")
print(min(list))
print("=-=-=" * 15)

print("Even Numbers")
for num in list:
    if num % 2 == 0:
        print(num)
print("=-=-=" * 15)

print("Odd Numbers")
for num in list:
    if num % 2 == 1:
        print(num)
print("=-=-=" * 15)

print("Positive Numbers")
for numb in list:
    if numb > 0:
        print(numb)
print("=-=-=" * 15)

print("Positive Numbers 2")
newlist = [n for n in list if n > 0]
print(newlist)
print("=-=-=" * 15)

factor = 5
print("Multiply list by ", factor)
multiplied_number = []
for num in list:
    multiplied_number.append(num * factor)
print(multiplied_number)
print("=-=-=" * 15)

print("Reverse a string")
string = "Alessandra".upper()
print("String = ", string)
print(string[::-1])