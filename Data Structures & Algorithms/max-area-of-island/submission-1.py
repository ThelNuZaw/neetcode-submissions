class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()
        area = 0

        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            count = 1
            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if nr >= len(grid) or nc >= len(grid[0]) or (nr,nc) in visit or nr < 0 or nc < 0 or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
                    count += 1
            return count

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = max(area, bfs(r,c))
        return area