class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = defaultdict(list)
        for a, b in edges:
            components[a].append(b)
            components[b].append(a)

        visit = set()
        def dfs(node):
            visit.add(node)
            for nei in components[node]:
                if not nei in visit:
                    dfs(nei)

        count = 0
        for node in range(n):
            if not node in visit:
                dfs(node)
                count += 1
        return count