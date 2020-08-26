# Task: Create a class Vehicle

class Vehicle:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"My car is a {self.make} {self.model} {self.year}."

car = Vehicle("Ford", "Focus", "2020")

print(car.description())

