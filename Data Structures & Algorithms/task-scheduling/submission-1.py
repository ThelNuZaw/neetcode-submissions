class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque() # [-c, idletime]
        while maxheap or q:
            time += 1
            if maxheap:
                freq = heapq.heappop(maxheap) + 1
                if freq:
                    q.append([freq, time + n])
            
            if q and time == q[0][1]:
                heapq.heappush(maxheap,q.popleft()[0])
        return time
                