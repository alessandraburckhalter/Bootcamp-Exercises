total = float(input("Total bill amount? "))
level = str(input("""\nLevel of service:
good -> 20%
fair -> 15%
bad -> 10%? """ )).lower()

tip1 = (total * 20) / 100
tip2 = (total * 15) / 100
tip3 = (total * 10) / 100

split = int(input("Split how many ways? "))


if level == "good":
    print('\nTip amount: $%.2f' %tip1)
    print('\nTotal amount: $%.2f' %(tip1 + total))
    print('\nAmount per person: $%.2f' %((tip1 + total) / split))

elif level == "fair":
    print('\nTip amount: $%.2f' %tip2)
    print('\nTotal amount: $%.2f' %(tip2 + total))
    print('\nAmount per person: $%.2f' %((tip2 + total) / split))

elif level == "bad":
    print('\nTip amount: $%.2f' %tip3)
    print('\nTotal amount: $%.2f' %(tip3 + total))
    print('\nAmount per person: $%.2f' %((tip3 + total) / split))