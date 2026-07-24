class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return[0]
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        edg_cnt = {}
        q = deque()
        for i, ed in adj.items():
            edg_cnt[i] = len(ed)
            if len(ed) == 1:
                q.append(i)

        while q:
            if n <= 2:
                return list(q)
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in adj[node]:
                    edg_cnt[nei] -= 1
                    if edg_cnt[nei] == 1:
                        q.append(nei)
        