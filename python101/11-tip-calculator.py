#Task: Write a program that calculates how much of a tip to leave at a restaurant.
#Prompt the user for two things:
#The total bill amount
#The level of service, which can be one of the following: good, fair, or bad
#Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:
#good -> 20%
#fair -> 15%
#bad -> 10%

total = float(input("Total bill amount? "))
level = str(input("""\nLevel of service:
good -> 20%
fair -> 15%
bad -> 10%? """ )).lower()

#Calculate the tip
tip1 = (total * 20) / 100
tip2 = (total * 15) / 100
tip3 = (total * 10) / 100


if level == "good":
    print('\nTip amount: $%.2f' %tip1)
    print('\nTotal amount: $%.2f' %(tip1 + total))

elif level == "fair":
    print('\nTip amount: $%.2f' %tip2)
    print('\nTotal amount: $%.2f' %(tip2 + total))

elif level == "bad":
    print('\nTip amount: $%.2f' %tip3)
    print('\nTotal amount: $%.2f' %(tip3 + total))