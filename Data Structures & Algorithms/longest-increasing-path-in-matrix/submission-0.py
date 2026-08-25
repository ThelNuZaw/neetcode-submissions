class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = {} #(r,c) -> LIP
        def dfs(r, c, val):
            if r >= row or r < 0 or c >= col or c < 0 or matrix[r][c] <= val:
                return 0

            if (r, c) in dp:
                return dp[(r,c)]
            res = 1 # count current cell itself
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r,c)] = res
            return res
        for r in range(row):
            for c in range(col):
                dfs(r, c, -1)
        return max(dp.values())