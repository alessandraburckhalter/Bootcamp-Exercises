# Using the dictionary from the Nested dictionaries exercise above, write a function countFriends() that accepts a dictionary as an argument and returns a new dictionary that includes a new key friends_count
def countFriends(a_dic):
   friends = 0
 #   for words in ramit:
 #       dic.append("friends_count")
 #   return dic


# dictionary
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# Write a python expression that gets the email address of Ramit.
print("Here is Ramit's email address: ", ramit['email'])

# Write a python expression that gets the first of Ramit's interests.
print("Here is Ramit's first interest: ", ramit['interests'][0])

# Write a python expression that gets the email address of Jasmine.
print("Here is Jasmine's address: ", ramit['friends'][0]['email'])

# Write a python expression that gets the second of Jan's two interests.
print("Here is Jan's second interest: ", ramit['friends'][1]['interests'][1])

# return the function 
# print(countFriends(ramit))