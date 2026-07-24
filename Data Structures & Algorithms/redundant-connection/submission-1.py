class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)] # [0,1,2,3,4]
        rank = [1] * (n + 1) # [1,1,1,1,1]
        
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(u, v):
            p1, p2 = find(u), find(v) # to find their respective parent

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []
        