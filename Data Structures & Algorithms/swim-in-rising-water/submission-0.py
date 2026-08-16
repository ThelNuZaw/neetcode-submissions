class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minheap = [[grid[0][0], 0, 0]] #max_time, r, c
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))

        while minheap:
            time, r, c = heapq.heappop(minheap)
            if r == n - 1 and c == n - 1:
                return time
            for dr, dc in directions:
                n_dr = dr + r
                n_dc = dc + c
                if (n_dr < 0 or n_dc < 0 or n_dr >= n or n_dc >= n or (n_dr, n_dc) in visit):
                    continue
                visit.add((n_dr, n_dc))
                heapq.heappush(minheap, [max(time, grid[n_dr][n_dc]), n_dr, n_dc])
