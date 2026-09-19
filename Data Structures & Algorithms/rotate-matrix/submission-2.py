class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix[0]) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                topleft = matrix[top][left + i]

                #bottom left to topleft
                matrix[top][left + i] = matrix[bottom - i][left]

                #bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                #top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                #top left to top right
                matrix[top + i][right] = topleft
            left += 1
            right -= 1
        

            