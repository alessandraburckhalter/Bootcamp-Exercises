#Task: Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user.

print("Enter a number in degrees Celsius and you'll get the value in degrees Fahrenheit.")
print("\nReady? Let's go!")

celsius = float(input("\nTemperature in C? "))

#formula 
F = (celsius * 9/5) + 32

print(f"\nThe temperature is {F} F.")