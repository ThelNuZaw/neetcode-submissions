class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        rows = [0] * n #1D last row
        rows[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    rows[j] = 0
                elif j + 1 < n:
                    rows[j] = rows[j] + rows[j + 1] #row below it. + right
                
        return rows[0]