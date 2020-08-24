# Dictionary
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

# Task: Print Elizabeth's phone number.
print("Here is Elizabeth's phone number: ", phonebook_dict['Elizabeth'])

# Task: Add an entry to the dictionary: Kareem's number is 938-489-1234.
phonebook_dict['Kareem'] = '938-489-1234'
print("\nKareem's phone number was added: ", phonebook_dict)

# Task: Delete Alice's phone entry.
phonebook_dict["Alice"] = ""
print("\nAlice's phone number was deleted: ", phonebook_dict)

# Change Bob's phone number to '968-345-2345'
for name, phone in phonebook_dict.items():
    if phone == "857-384-1234":
        phonebook_dict[name] = "968-345-2345"
        print("\nBob's phone number was replaced: ", phonebook_dict)

# Print all the phone entries
print("\nAll phone numbers: ",phonebook_dict.values())