class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        visit = set()
        heap = [[0,0,0]] #[diff, r, c]
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r,c) in visit:
                continue
            visit.add((r,c))

            if (r,c) == (rows - 1, cols - 1):
                return diff
            for dr, dc in directions:
                newdr = dr + r
                newdc = dc + c
                if newdr < 0 or newdc < 0 or newdr >= rows or newdc >= cols or (newdr, newdc) in visit:
                    continue
                newdiff = max(diff, abs(heights[newdr][newdc] - heights[r][c]))
                heapq.heappush(heap, [newdiff, newdr, newdc])
            


