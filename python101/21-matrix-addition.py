#Task: Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists. Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices.

matrix1 = [[1, 3], [2, 4]]

matrix2 = [[5, 2],
1,0]

for line in range(0, 2):
    for row in range(0, 2):
       print(f"{matrix1[line][row]:^5}", end=" ")