def stockSpan(arr):
    countArray = []
    for i in range(len(arr)):
        count = 1
        for j in range(i):
            if(arr[i] >arr[j]):
                count+=1
            else:
                count = 1

        countArray.append(count)
    return countArray

#optimized version using stack

# basically we are tryin to store latest maximum, 
#   if we are trin to store the latest maximum then we will only need one param right?
#   yes but in this get we can get more than one maxima consider this case [100, 1, 2, 10, 9, 2, 3]

def stockSpanOptimized(price, n):
    stk = list()
    output = [-1]*n

    stk.append(0)
    output[0] = 1

    for i in range(1, n):
        while ( not isEmpty(stk) and (price[top(stk)] < price[i])):
            stk.pop()
        
        if isEmpty(stk):
            output[i] = i + 1
        else: 
            output[i] = i - top(stk)
        
        stk.append(i)
    
    return output

def isEmpty(arr):
    return len(arr) == 0

def top(arr):
    return arr[-1]


arr = [10, 10, 10, 10]

print(stockSpan(arr))

print(stockSpanOptimized(arr, len(arr)))


#takeInput 
n = int(input())
priceArray = list(map(int, input().split()))
print(stockSpanOptimized(priceArray, len(priceArray)))

# 8
# 60 70 80 100 90 75 80 120
# Ans : [1, 2, 3, 4, 1, 1, 2, 8]