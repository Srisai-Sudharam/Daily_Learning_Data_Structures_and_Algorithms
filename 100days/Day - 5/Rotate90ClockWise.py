class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(r-l):
                top = left
                bottom = right #since this is a square matrix


                topLeft = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left]

                matrix[bottom - i][left] = matrix[bottom][right - i]

                matrix[bottom][right - i] = matrix[top + i][right]
                
                matrix[top + i][right] = topLeft


        