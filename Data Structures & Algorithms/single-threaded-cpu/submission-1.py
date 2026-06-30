class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i) #put its original index before sorting [start, processing, index]
        tasks.sort(key = lambda t : t[0]) #sorted by the start time
        minheap = []
        res = [] # index
        time = tasks[0][0] # min
        i = 0
        while minheap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minheap, [tasks[i][1], tasks[i][2]])
                i += 1

            # when cpu idle time
            if not minheap:
                time = tasks[i][0] 
            else:
                processing_time, index = heapq.heappop(minheap)
                time += processing_time
                res.append(index)
        return res
