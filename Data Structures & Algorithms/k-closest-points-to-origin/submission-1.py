class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            distance = -((x ** 2) + (y ** 2))
            heapq.heappush(maxheap, [distance, x, y])
            
            while len(maxheap) > k:
                heapq.heappop(maxheap)
        res = []
        while maxheap:
            dist, x, y = heapq.heappop(maxheap)
            res.append([x,y])
        return res
        

        