class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # row
        n = len(grid[0]) #col
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n] = 0 # below the last cell min(0, inf)

        for i in range(m - 1, -1, -1):
            for j in range(n -1, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]