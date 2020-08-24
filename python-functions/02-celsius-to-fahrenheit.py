# Task: Write a function that takes a temperature in Fahrenheit, converts it to Celsius, and returns the value.

# create the function
def conversion(temperature):
    formula = (temperature * 9/5) + 32
    return f"{temperature}C equals to {formula}F."

# ask user to input a number
temperature = int(input("Please, enter the temperature you would like to convert:\n> "))
# print function
print(conversion(temperature))