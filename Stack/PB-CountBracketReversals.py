
from sys import stdin

def countBracketReversals(inputString) :
    n = len(inputString)
    if(n%2 !=0):
        return -1
    stk = list()
    revOps = 0
    
    for i in range(n):
        if isEmpty(stk):
            if inputString[i] == '}':
                revOps+=1
                stk.append("{")
            else:
                stk.append("{")
        elif inputString[i] == '}':
            stk.pop()
        else:
            stk.append("{")
        
        
    revOps += len(stk) // 2
    return revOps




def isEmpty(stack):
    return len(stack) == 0


#main
print(countBracketReversals(stdin.readline().strip()))
