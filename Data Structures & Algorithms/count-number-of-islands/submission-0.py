class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        island = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                rpop, cpop = q.popleft()
                directions = [[0,-1], [0,1], [-1,0], [1,0]]
                for dr, dc in directions:
                    r = rpop + dr
                    c = cpop + dc
                    if(r in range(row) and c in range(col) and grid[r][c] == "1" and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(row):
            for c in range(col):
                if(grid[r][c] == "1" and (r,c) not in visited):
                    bfs(r, c)
                    island += 1
        return island
