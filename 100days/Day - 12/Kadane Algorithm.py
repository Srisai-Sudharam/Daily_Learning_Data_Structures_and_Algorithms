from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

#here I have set max_sum, curr_sum to zero since it is mentioned in problem to consider empty set

# other wise set them to arr[0] and traverse from 1 to len(arr) - 1

def maxSubarraySum(arr, n) :
    max_current, max_sum = 0, 0
    for i in range(len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_sum:
            max_sum = max_current
    
    return max_sum




























#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
