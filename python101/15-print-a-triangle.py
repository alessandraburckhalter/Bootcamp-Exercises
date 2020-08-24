rows = 10
count = 0

while count < rows:
    output = ""
    output += " " * (rows - count)
    output += "*" * (count * 2 + 1)
    count += 1
    print(output)


    