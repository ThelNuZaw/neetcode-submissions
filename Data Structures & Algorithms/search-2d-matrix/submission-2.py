class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        isexist = False
        rows, cols = len(matrix), len(matrix[0])
        top = 0
        bottom = rows - 1
        while top <= bottom:
            prow = (top + bottom) // 2
            if target > matrix[prow][-1]:
                top = prow + 1
            elif target < matrix[prow][0]:
                bottom = prow - 1
            else:
                break
        if not (top <= bottom):
            return (isexist)
        left, right = 0, cols - 1
        prow = (top + bottom) // 2
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[prow][middle]:
                left = middle + 1
            elif target < matrix[prow][middle]:
                right = middle - 1
            else:
                isexist = True
                break
        return (isexist)
