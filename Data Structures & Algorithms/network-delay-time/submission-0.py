class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for ui, vi, ti in times:
            edges[ui].append((vi,ti))

        minheap = [(0, k)]
        weight = 0
        visit = set()
        
        while minheap:
            t, u = heapq.heappop(minheap)
            if u in visit:
                continue
            visit.add(u)
            weight = max(weight, t)
            for nei_v, nei_t in edges[u]:
                if not nei_v in visit:
                    heapq.heappush(minheap, (nei_t + t, nei_v))
        return weight if len(visit) == n else -1