from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    lis = []
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                lis.append([i, j])

    for i in lis:
        rows, cols = i[0], i[1]
        for j in range(c):
            matrix[rows][j] = 0
        for k in range(r):
            matrix[k][cols] = 0 
