#Brute Force
# def subArrayCount(arr, k):
#     length = len(arr)
#     count = 0
#     longest_sub_array = 0
#     for i in range(length):
#         for j in range(i+1, length+1):
#             if sum(arr[i:j]) % k == 0:
#                 count += 1
#     return count                 

# optimized   

def subArrayCount(arr, k):
    remMap = {}   
    remMap[0] = 1  

    count = 0
    summ = 0
    for i in range(len(arr)):
        summ += arr[i]

        rem = summ % k
        # If rem already in 'remMap'.
        if(rem in remMap):
            count += remMap[rem]
            remMap[rem] += 1
        else:
            remMap[rem] = 1

    return count