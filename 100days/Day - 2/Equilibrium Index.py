def equilibruimIndex(arr):
    n = len(arr)
    arraySum = sum(arr)
    leftSum = 0
    for i in range(n):
        if leftSum == arraySum - leftSum - arr[i]:
            return i
        leftSum += arr[i]
    return -1

#O(N)
#O(1)