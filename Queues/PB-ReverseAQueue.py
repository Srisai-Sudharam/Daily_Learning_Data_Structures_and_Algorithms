
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    if inputQueue.empty():
        return 
    # Your code goes here
    ele = inputQueue.get()
    reverseQueue(inputQueue)
    inputQueue.put(ele)



'''-------------- Utility Functions --------------'''



def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1


# t = no of test cases
# 1
# 7
# 2 8 5 1 10 5 9 
