from typing import List

# def setZeros(matrix: List[List[int]]) -> None:
#     lis = []
#     r = len(matrix)
#     c = len(matrix[0])
#     for i in range(r):
#         for j in range(c):
#             if matrix[i][j] == 0:
#                 lis.append([i, j])

#     for i in lis:
#         rows, cols = i[0], i[1]
#         for j in range(c):
#             matrix[rows][j] = 0
#         for k in range(r):
#             matrix[k][cols] = 0 

#Approach -2 

# maintain two arrays one for columns and other for rows space = O(m+n)
    #  __ __ __
    # |X |X |  |
    #  -- -- -- 
#  __
# |X | 0  1  1
# |  | 1  1  1
# |X | 1  0  1
# ----

# In above diagram there are two array that kee track of which row or columns to be made zero


# Approach 3 inplace space complexity = o(1) 

# we just stored the value inside matrix itself rather than storing them in seperate arrays
    
#  |0|  |1|  |1| <-- columns array
#  |1|    1    1
#  |1|   0    1 
#   ^
# row array

# since the column array is occupying the first row completely we used another temp variable rowZero to keep track of 0th row



def setZeros(matrix: List[List[int]]) -> None:
    row, col  = len(matrix), len(matrix[0])
    rowZero = False

    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 0:
                matrix[0][c] = 0

                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
    

    for r in range(1, row):
        for c in range(1, col):
            if matrix[r][0] == 0 or matrix[0][c] ==0:
                matrix[r][c] = 0
    
    if matrix[0][0] == 0:
        for r in range(row):
            matrix[r][0] = 0
    
    if rowZero:
        for c in range(col):
            matrix[0][c] = 0


