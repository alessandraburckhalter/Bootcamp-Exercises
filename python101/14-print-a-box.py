#Task: Given a height and width, input by the user, print a box consisting of * characters as its border.

w = int(input("Width? "))
h = int(input("Height? "))

count = 1

while count <= h:
    if count == 1 or count == h:
        output = "*" * w 
    else:
        output = "*" 
        output += " " * (w - 2)
        output += "*"
    count += 1
    print(output)


    

    