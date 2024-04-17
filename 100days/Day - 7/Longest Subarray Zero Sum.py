#Brute Force
# O(N^2)time , O(1) space
# def LongestSubsetWithZeroSum(arr):
#     length = len(arr)
#     longest_sub_array = 0
#     for i in range(length):
#         for j in range(i+1, length+1):
#             if sum(arr[i:j]) == 0 and len(arr[i:j]) > longest_sub_array:
#                 longest_sub_array = len(arr[i:j])
#     return longest_sub_array                    


# optimal approach using hash maps O(N), O(N)
    #   10 + [...] = 10
    #   sum + 0    = sum

def LongestSubsetWithZeroSum(arr):
    hash_map = {}
    max_len = 0   
    curr_sum = 0
     
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0:
            max_len = i + 1
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i
 
    return max_len