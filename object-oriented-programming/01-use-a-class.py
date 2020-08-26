# Given the following Person class:
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        self.greeting_count += 1     
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def contact_info(self):
        print(f"Name: {self.name}:\nPhone: {self.phone}\nEmail: {self.email}")

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# Write a print statement to print the contact info (email and phone) of Sonny.
print(sonny.name, sonny.phone)
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
print("--" * 15)
# Write another print statement to print the contact info of Jordan.
print(jordan.name, jordan.email, jordan.phone)
print("--" * 15)
# Have  jordan greet  sonny using the greet method.
jordan.greet(sonny)
# Have sonny greet  jordan using the greet method.
sonny.greet(jordan)
print(f"Sonny introduced himself {sonny.greeting_count} time.")
print(f"Jordan introduced himself {jordan.greeting_count} time.")
print("--" * 15)
#  Add a contact_info method to the Person class that will print out the contact info for a object instance of Person.
sonny.contact_info()
print("--" * 15)
jordan.contact_info()
print("--" * 15)
# append a friend to Sonny
sonny.add_friend(jordan)
# print how many friends were appended
print(f"Sonny has {sonny.num_friends()} friends.")
# create a loop to print Sonny friend's name
for friend in sonny.friends:
    print(friend.name)



