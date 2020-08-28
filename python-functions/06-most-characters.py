# write a function called most_characters that accepts a string, and return the character that appears the most.

# create an empty dictionary to store the string
result = {}

# create a function to verify if the string is already in the dictionary and enumerate them
def most_characters(string):
    for letter in string.lower():
        if letter in result.keys():
            result[letter] += 1
        else:
            result[letter] = 1
# use the max function to get the letter that appears the most
    return max(result, key=result.get)

# print function       
print(most_characters("abCCcdDDDDa"))