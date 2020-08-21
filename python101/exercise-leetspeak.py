text = input("Type a sentence: ").upper()

leet = ' '

for x in text:
    if x == 'A':
        leet += '4'
    elif x == 'E':
        leet += '3'
    elif x == 'G':
        leet += '6'
    elif x == 'I':
        leet += '1'
    elif x == 'O':
        leet += '0'
    elif x == 'S':
        leet += '5'
    elif x == 'T':
        leet += '7'
    else:
        leet += x

print(leet)



