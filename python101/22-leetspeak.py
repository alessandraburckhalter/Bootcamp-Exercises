#Task: Given a paragraph of text as a String, print the paragraph in leetspeak.

text = input("Type a sentence: ").upper()

leet = ' '

for letter in text:
    if letter == 'A':
        leet += '4'
    elif letter == 'E':
        leet += '3'
    elif letter == 'G':
        leet += '6'
    elif letter == 'I':
        leet += '1'
    elif letter == 'O':
        leet += '0'
    elif letter == 'S':
        leet += '5'
    elif letter == 'T':
        leet += '7'
    else:
        leet += x

print(leet)



