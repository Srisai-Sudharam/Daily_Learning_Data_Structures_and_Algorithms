
# Brute Force 
    # Time - O(NlogN)
    # Space - O(1)

# def separateNegativeAndPositive(nums):
#     # write your code here
#     nums.sort()

#     return nums




# elegant solutions using partitiong approach from Quicksort 
# # time - O(N), space - O(1)
# def separateNegativeAndPositive(nums):
#     # write your code here
#     j = 0

#     for i in range(len(nums)):
#         if nums[i] < 0:

#             if i != j:
#                 nums[i], nums[j] = nums[j], nums[i]
            
#             j+=1

#     return nums


# using two pointers left and right
# # time - O(N), space - O(1) same as quicksort approach
def separateNegativeAndPositive(nums):
    # write your code here

    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] < 0 and nums[right] < 0:
            left += 1
        elif nums[left] >= 0 and nums[right] >=0:
            right -= 1
        elif nums[left] >= 0 and nums[right] < 0:
            nums[left], nums[right]  = nums[right], nums[left]
        else:
            left += 1
            right -=1
    return nums