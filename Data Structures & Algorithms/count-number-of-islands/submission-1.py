class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        island = 0

        def backtrack(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0" or (i, j) in visit:
                return 
            visit.add((i, j))
            backtrack(i, j + 1)
            backtrack(i, j - 1)
            backtrack(i - 1, j)
            backtrack(i + 1, j)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    backtrack(r, c)
                    island += 1
        return island
