class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        top = 0
        bottom = ROW - 1

        while top <= bottom:
            middle_row = (top + bottom) // 2
            if target > matrix[middle_row][-1]:
                top = middle_row + 1
            elif target < matrix[middle_row][0]:
                bottom = middle_row - 1
            else:
                break
        if not(top <= bottom):
            return False
        left = 0
        right = COL - 1
        middle_row = (top + bottom) // 2
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[middle_row][middle]:
                left = middle + 1
            elif target < matrix[middle_row][middle]:
                right = middle - 1
            else:
                return True
        return False
