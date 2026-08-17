class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(n, adj, visit, path, order):
            if n in path:
                return False
            if n in visit:
                return True
            visit.add(n)
            path.add(n)
            for nei in adj[n]:
                if not dfs(nei, adj, visit, path, order):
                    return False
            path.remove(n)
            order.append(n)
            return True
        
        def topological(edges):
            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)
            visit, path = set(), set()
            order = [] # store num in order
            for n in range(1, k + 1):
                if not dfs(n, adj, visit, path, order):
                    return []
            return order[::-1]

        row_order = topological(rowConditions)
        col_order = topological(colConditions)

        if not row_order or not col_order:
            return []

        index_row = {n : i for i, n in enumerate(row_order)}
        index_col = {n: i for i, n in enumerate(col_order)}

        res = [[0] * k for _ in range(k)] #2D matrix
        for num in range(1, k + 1):
            r, c = index_row[num], index_col[num]
            res[r][c] = num
        return res

