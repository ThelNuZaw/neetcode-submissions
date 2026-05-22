class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for n in nums:
            heapq.heappush(maxheap, -n)
        
        while k > 0:
            ele = heapq.heappop(maxheap)
            k -= 1
        return -ele
