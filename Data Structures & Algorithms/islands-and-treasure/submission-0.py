class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        row, col = len(grid), len(grid[0])
        visited = set()
        step = 0
        q = collections.deque()

        def direction(r,c):
            if(r < 0 or r == row or c < 0 or c == col or grid[r][c] == -1 or (r,c) in visited):
                return
            q.append([r,c])
            visited.add((r,c))

        for r in range(row):
            for c in range(col):
                if(grid[r][c] == 0):
                    q.append([r,c])
                    visited.add((r,c))
        while q:
            for i in range(len(q)): #bfs layer starts and have to iterate all ele(r,c) in this layer
                rpop, cpop = q.popleft()
                grid[rpop][cpop] = step

                direction(rpop + 1, cpop)
                direction(rpop - 1, cpop)
                direction(rpop, cpop + 1)
                direction(rpop, cpop - 1)
            step += 1

        
