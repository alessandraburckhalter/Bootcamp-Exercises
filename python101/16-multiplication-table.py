#Task: Print the multiplication table for numbers from 1 up to 10. 

for numbers in range(1, 11):
    for num in range(1, 11):
        print(f"{numbers} x {num} = {numbers * num}\n")