

def inplaceRotate(inputArray, n):
    left, right = 0, len(inputArray) - 1
    while left < right:
        for i in range(right-left):
            top = left
            bottom = right

            #store top left in a temporary variable
            topLeft = inputArray[top][left + i]

            #move top right to top left
            inputArray[top][left + i] = inputArray[top + i][right]

            #move bottom right to top right
            inputArray[top + i][right] = inputArray[bottom][right - i]

            #move bottom left to bottom rigt
            inputArray[bottom][right - i] = inputArray[bottom - i][left]

            #move top left to bottom left
            inputArray[bottom - i][left] = topLeft
        
        left += 1
        right -= 1
    
    return inputArray 