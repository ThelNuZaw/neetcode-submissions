class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        while left < right and top < bottom:
            # every i in top row
            for i in range(left, right): #col change
                res.append(matrix[top][i])
            top += 1

            #for every i in right col
            for i in range(top, bottom): #row change
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom): # for 1*1 matrix
                break

            #for every i in bottom row
            for i in range(right - 1, left - 1, -1): #col change
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            #for every i in left col
            for i in range(bottom - 1, top - 1, -1): #row change
                res.append(matrix[i][left])
            left += 1
        return res