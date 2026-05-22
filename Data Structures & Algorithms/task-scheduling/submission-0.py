class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [ -c for c in count.values()]

        heapq.heapify(maxheap)
        time = 0
        q = deque()
        while maxheap or q:
            time += 1
            if maxheap: 
                hp = 1 + heapq.heappop(maxheap)
                if hp:
                    q.append([hp, time + n])
            
            if q and q[0][1] == time:
                qp = q.popleft()[0]
                heapq.heappush(maxheap, qp)
        return time 
            

            