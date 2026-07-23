class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = defaultdict(list)

        def dfs(node, pre):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == pre:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visit = set()
            if not dfs(a, -1):
                return [a, b]
        return []