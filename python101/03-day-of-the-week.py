#Task: The user will enter a number from 0 to 6. Given this number, print a day of the week. 0 for Sunday, 1 for Monday, 2 for Tuesday, and so on.

print("Enter a number from 0 to 6.")

for num in range(0, 7):
    day = int(input("Day (0-6)? "))
    if day == 0:
        print("Sunday")
    elif day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    else:
        print("Wrong option")