# Task: You will write a command line program to manage a phone book.
# If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
# If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
# If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
# If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
# If they choose to quit, end the program.

print("=-=" * 20)
print("               Electronic Phone Book")
print("=-=" * 20)

# create an empty dictionary to store the user input
phonebook = {}

while True:
    user = int(input("\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit\nWhat do you want to do (1-5)?\n> "))

    if user == 1:
        name = str(input("\nPlease, enter the person's name:\n> ")).upper()
        if name in phonebook.keys():
            print(f"Found entry for {name}.\nName: {phonebook[name]['name']}\nPhone: {phonebook[name]['phone']}.")
        else:
            print("\nThis person is not part of your contacts. Please, go back to the main menu and choose option 2 to set a new entry.")

    if user == 2:
        name1 = str(input("\nPlease, enter the person's name you would like to add:\n> ")).upper()
        phone = int(input("\nPlease, enter the phone number:\n> "))
        # set the variable names for the user input to store in the dictionary
        phonebook[name1] = {
            'name': name1,
            'phone': phone
        }
        print(f"\nName: {phonebook[name1]['name']}\nNumber: {phonebook[name1]['phone']}")
        print(f"\nEnter stored for {name1}.")

    if user == 3:
        name2 = str(input("\nWhat is the name of the person you would like to delete?\n> ")).upper()   
        if name2 in phonebook.keys():
        # use pop() to delete the entry
            phonebook.pop(name2)
            print(f"Deleted enter for {name2}.")
        else:
            print(f"I'm sorry, but {name2} is not part of your contacts.")

    if user == 4:
    # use for to loop through the phonebook and print all contacts
        for name in phonebook.keys():
            print(f"\nName: {phonebook[name]['name']}\nNumber: {phonebook[name]['phone']}")

    if user == 5:
        print("\nSee you soon :)")
        break

