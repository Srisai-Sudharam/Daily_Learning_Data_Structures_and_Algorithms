from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

#High, Low, Mid

def sort012(arr, n) :

    low, mid = 0, 0
    high = n - 1

    while mid <= high:
        if arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        elif arr[mid] == 0:
            arr[mid], arr[low]= arr[low], arr[mid]
            low += 1
            mid += 1  
        else:
            mid += 1



#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
