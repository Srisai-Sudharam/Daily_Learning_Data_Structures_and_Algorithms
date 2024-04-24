# Brute Force O(N^2), O(1)
# def maxArea(height):
#     length = len(height)
#     maxArea = 0
#     for i in range(length):
#         for j in range(i+1, length):
#             area = min(height[i], height[j]) * (j-i)
#             maxArea = max(area, maxArea)
#     return maxArea
        
#Optimized approach
# O(1), O(1)
# two pointer approach the pointers are moved based on the height of the line

def maxArea(height):
    length = len(height)
    i = 0
    j = length - 1
    maxArea = 0

    while i < j:
        area = (j-i) * min(height[i], height[j])
        
        maxArea = max(area, maxArea)

        if height[i] <= height[j]:
            i+=1
        else:
            j-=1
    return maxArea

