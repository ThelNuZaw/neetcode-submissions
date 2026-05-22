class MedianFinder:

    def __init__(self):
    # initialize my data structure 
    # use two heaps: small for max and large for min 
    # so that we can know the correct middle element of array[1,2] [3,4,5]>> just take 3 off the large using minO(1)

        self.small = [] # store - values
        self.large = [] # store + values

    def addNum(self, num: int) -> None:
        # there are conditions need to check 
        #if element from smalll <= large
        # if diff of len(small) and len(large) should be 1 and less
        heapq.heappush(self.small, -1 * num) # for max heap 

        if (self.small and self.large and -1 * self.small[0] > self.large[0]): # -1 * to delete the - and push original value to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if (len(self.small) > len(self.large) + 1): # small is bigger than 2 and pop from small 
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if (len(self.large) > len(self.small) + 1): # large is bigger than 2 and pop from large
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val) # to get - values to small
    def findMedian(self) -> float:
        if (len(self.small) > len(self.large)):
            return -1 * self.small[0] 
        if (len(self.large) > len(self.small)):
            return self.large[0]
        return ((-1* self.small[0] + self.large[0])/2)

        
        