# Brute Force O(N^2), O(1)
def maxArea(height):
    length = len(height)
    maxArea = 0
    for i in range(length):
        for j in range(i+1, length):
            area = min(height[i], height[j]) * (j-i)
            maxArea = max(area, maxArea)
    return maxArea
            