#Task: Prompt the user for a day of the week just like the previous problem. But this time, print "Go to work" if it's a work day and "Sleep in" if it's a weekend day. 

print("New week ahead!")
print("Enter a number from 0 to 6.")

for num in range(0, 7):
    day = int(input("Day (0-6)? "))
    if day == 0:
        print("It's Sunday! Sleep in.")
    elif day == 1:
        print("Monday. Go to work.")
    elif day == 2:
        print("Tuesday. Go to work.")
    elif day == 3:
        print("Wednesday. Go to work.")
    elif day == 4:
        print("Thursday. Go to work.")
    elif day == 5:
        print("Happy Friday! Go to work.")
    elif day == 6:
        print("It's Saturday! Sleep in.")
    else:
        print("Wrong option")