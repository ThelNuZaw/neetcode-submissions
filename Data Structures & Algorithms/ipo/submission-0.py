class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap = [ [c, p] for c, p in zip(capital, profits)]
        heapq.heapify(minheap)
        maxprofit = []

        for i in range(k):
            while minheap and minheap[0][0] <= w:
                c, p = heapq.heappop(minheap)
                heapq.heappush(maxprofit, -1 * p)
            if not maxprofit:
                break
            w += -1 * heapq.heappop(maxprofit)
        return w