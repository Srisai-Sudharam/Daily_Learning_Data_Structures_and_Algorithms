def isMatrixSymmetric(matrix):
    nc = len(matrix[0])
    nr = len(matrix)
    for i in range(nc):
        for j in range(nr):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
