class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        fresh = 0
        for r in range(row):
            for c in range(col):
                if(grid[r][c] == 1):
                    fresh += 1
                if(grid[r][c] == 2):
                    q.append([r,c])
                    visited.add((r,c))
        minute = 0
        while q and fresh > 0:
            for i in range(len(q)):
                
                rp, cp = q.popleft()
                direction = [[0,1], [0,-1], [1,0], [-1, 0]]
                for dr, dc in direction:
                    r = rp + dr
                    c = cp + dc
                    if(r not in range(row) or c not in range(col) or (r,c) in visited or grid[r][c] != 1 ):
                        continue
                    q.append([r,c])
                    visited.add((r,c))
                    fresh -= 1
               
            minute += 1
        return minute if fresh == 0 else -1
                    