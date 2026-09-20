class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        alt = set()
        
        def dfs(visit, preh, r, c):
            if (r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visit or preh > heights[r][c]):
                return 
            visit.add((r,c))
            dfs(visit, heights[r][c], r + 1, c)
            dfs(visit, heights[r][c], r - 1, c)
            dfs(visit, heights[r][c], r , c + 1)
            dfs(visit, heights[r][c], r, c - 1)

        for c in range(cols):
            dfs(pac, heights[0][c], 0, c)
            dfs(alt, heights[rows - 1][c], rows - 1, c)
        
        for r in range(rows):
            dfs(pac, heights[r][0], r, 0)
            dfs(alt, heights[r][cols - 1], r, cols - 1)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in alt:
                    res.append((r,c))
        return res
        