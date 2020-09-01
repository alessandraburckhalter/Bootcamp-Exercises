#Task: Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program.

print("\nLet's play!")
print("\nYou have 0 coins.")

#Starts the counter on 0
count = 0


while True: 
    question = str(input("\nDo you want another? ")).lower()
    if question == "yes":
        count += 1
        print(f"Now you have {count} coins.")

    else:
        print("Ok, bye.")
        break