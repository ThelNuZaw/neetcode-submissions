class MedianFinder:

    def __init__(self):
        self.minheap = [] #right large half
        self.maxheap = [] #left small half

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -1 * num)
        
        if len(self.minheap) > len(self.maxheap) + 1:
            min_num = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,  -1 * min_num)
        if len(self.maxheap) > len(self.minheap) + 1:
            max_num = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -1 * max_num)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.maxheap) > len(self.minheap):
            return self.maxheap[0] * -1
        else:
            return ((self.maxheap[0] * -1) + self.minheap[0]) / 2
        