print("\nLet's play!")
print("\nYou have 0 coins.")


count = 0


while True: 
    question = str(input("\nDo you want another? ")).lower()
    if question == "yes":
        count += 1
        print(f"Now you have {count} coins.")

    else:
        print("Ok, bye.")
        break