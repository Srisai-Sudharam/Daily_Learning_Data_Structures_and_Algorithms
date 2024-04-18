#Brute Force
def subArrayCount(arr, k):
    length = len(arr)
    count = 0
    longest_sub_array = 0
    for i in range(length):
        for j in range(i+1, length+1):
            if sum(arr[i:j]) % k == 0:
                count += 1
    return count                    