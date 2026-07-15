class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def backtrack(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i,j))
            perm = backtrack(i, j + 1)
            perm += backtrack(i - 1, j)
            perm += backtrack(i + 1, j)
            perm += backtrack(i, j - 1)
            return perm

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return backtrack(i, j)
        