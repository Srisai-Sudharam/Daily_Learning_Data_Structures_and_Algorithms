from sys import stdin

def spiralPrint(mat, nRows, mCols):
    
    l, t = 0 ,0
    r, b = mCols -1, nRows - 1 

    while (l < r or t < b):
        #top row
        for i in range(l, r):
            print(mat[t][i], end = " ")
        #right column 
        for i in range(t, b):
            print(mat[i][r], end = " ")
        #bottom row
        for i in range(l, r):
            print(mat[b][mCols-i-1], end = " ")
        #left column
        for i in range(t, b):
            print(mat[nRows-i-1][l], end = " ")
        
        l += 1 
        r -= 1
        t += 1
        b -= 1






















#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1