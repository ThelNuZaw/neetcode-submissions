class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()
        count = 0
        def dfs(n):
            visit.add(n)
            for nei in graph[n]:
                if nei not in visit:
                    dfs(nei)

        for i in range(n):
            if not i in visit:
                dfs(i)
                count += 1
        return count