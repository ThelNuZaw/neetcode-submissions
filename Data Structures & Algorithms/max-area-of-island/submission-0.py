class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        area = 0
        visited = set()
        def bfs(r, c):
            q = collections.deque()
            count = 1
            q.append((r,c))
            visited.add((r,c))
            while q:
                ro,co = q.popleft()
                directions = [[1,0], [-1,0],[0,-1], [0,1]]
                for dr, dc in directions:
                    r = ro + dr
                    c = co + dc
                    if(r in range(row) and c in range(col) and grid[r][c] == 1 and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
                        count += 1
            return count

        for r in range(row):
            for c in range(col):
                if(grid[r][c] == 1 and (r,c) not in visited):
                    a_count = bfs(r,c)
                    area = max(area, a_count)
        return area
