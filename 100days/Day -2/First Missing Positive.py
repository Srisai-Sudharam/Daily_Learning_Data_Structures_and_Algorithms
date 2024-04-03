

def firstMissing(arr, n):
    # Write your function here.
    length = len(arr)

    for i in range(length):
        if arr[i] < 0:
            arr[i] = 0
    
    for i in range(length):
        val = abs(arr[i]) 
        if val >= 1 and val <= length:
            
            if arr[val - 1] > 0:
                arr[val - 1]  *=  -1
            elif arr[val-1] == 0:
                arr[val-1] = -1 * (length + 1)
    
    for i in range(1, length + 1):
        if arr[i - 1] >= 0:
            return i
    return length + 1
    



    

# Main Code
t=int(input())

for j in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    ans = firstMissing(arr,n)

    print(ans)
