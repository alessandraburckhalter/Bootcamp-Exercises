#Task: Same as the previous problem, except you will prompt the user for the number to start on and the number to end on.

start = int(input("Start from: "))
end = int(input("End on: "))

for data in range(start, end + 1):
    print(data)
