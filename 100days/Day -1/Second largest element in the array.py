from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    
    secondLargest = -sys.maxsize + 1
    largest = -sys.maxsize + 1

    for ele in sequenceOfNumbers:
        if ele > largest:
            secondLargest = largest
            largest = ele
        elif ele > secondLargest and ele != largest:
            secondLargest = ele
        
    if secondLargest == -sys.maxsize + 1:
        return -1
    else:
        return secondLargest















# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
