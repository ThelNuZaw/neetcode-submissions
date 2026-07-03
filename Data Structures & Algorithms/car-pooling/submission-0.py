class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # #O(nlogn)
        # trips.sort(key = lambda t : t[1]) #start time
        # minheap = [] #(endtime, passenger)
        # cur = 0

        # for t in trips:
        #     passenger, start, end = t
        #     #drop off condition
        #     while minheap and minheap[0][0] <= start:
        #         cur -= minheap[0][1]
        #         heapq.heappop(minheap)

        #     cur += passenger
        #     if cur > capacity:
        #         return False
        #     heapq.heappush(minheap,[end, passenger])
            
        # return True

        #O(n)
        passChange = [0] * 1001
        curpass = 0
        for t in trips:
            numpass, start, end = t
            passChange[start] += numpass
            passChange[end] -= numpass

        for i in range(1001):
            curpass += passChange[i]
            if curpass > capacity:
                return False
        return True