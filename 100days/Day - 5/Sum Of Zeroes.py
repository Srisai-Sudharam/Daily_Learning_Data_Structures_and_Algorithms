from os import *
from sys import *
from collections import *
from math import *

def coverageOfMatrix(a):
    # Write your code here.
    nc = len(a[0])
    nr = len(a)
    
    coverage = 0
    for i in range(nr):
        for j in range(nc):
            if a[i][j] == 0:
                if i > 0:
                    coverage += a[i-1][j]
                if j > 0:
                    coverage += a[i][j-1]
                if i < nr -1:
                    coverage += a[i+1][j]
                if j < nc -1:
                    coverage += a[i][j+1]
    return coverage