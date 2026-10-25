class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)

        q = deque()
        time = 0
        while maxheap or q:
            time += 1
            if maxheap:
                v = heapq.heappop(maxheap) + 1
                if v:
                    q.append([v, time + n])
            if q and time == q[0][1]:
                heapq.heappush(maxheap, q.popleft()[0])
        return time


          