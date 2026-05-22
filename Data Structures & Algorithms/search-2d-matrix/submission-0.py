class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        left = 0
        isexist = False


        for i in range(len(matrix)):
    
            right = len(matrix[i]) - 1
            if(matrix[i][left] <= target <= matrix[i][right]):
                while left <= right:
                    mid = (left + right)//2
                    if(matrix[i][mid] == target):
                        isexist = True
                        break
                    elif(matrix[i][mid] < target):
                        left = mid + 1
                    else:
                        right = mid - 1
        return(isexist)
