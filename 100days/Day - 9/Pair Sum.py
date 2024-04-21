"""
    Time complexity: O(N) # since the array is already sorted
    Space complexity: O(1)
"""

def pairSum(arr, n, target): 
    
    countPair = 0

    start = 0
    end = n - 1

    
    while (start < end): 
        
        if (arr[start] + arr[end] == target):
            countPair += 1
            
            start += 1
            end -= 1
        
        
        elif (arr[start] + arr[end] < target): 
            start += 1
         
        
        else:
            end -= 1
        
    
    if (countPair == 0):
        return -1
     
    
    return countPair