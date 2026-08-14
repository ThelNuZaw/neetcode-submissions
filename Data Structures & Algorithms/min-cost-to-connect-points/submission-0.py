class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)} #(cost, node)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        minheap = [[0,0]]
        res = 0
        visit = set()

        while len(visit) < n:
            cost, node = heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            res += cost

            for nei_cost, nei_node in adj[node]:
                if nei_node not in visit:
                    heapq.heappush(minheap, [nei_cost, nei_node])
        return res
