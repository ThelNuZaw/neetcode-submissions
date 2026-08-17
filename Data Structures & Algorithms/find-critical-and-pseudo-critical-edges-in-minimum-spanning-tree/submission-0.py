class Union:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, p):
        while p != self.par[p]:
            p = self.par[p]
        return p

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2: #find cycle 
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
    
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i) #[v1, v2, weight, i]

        edges.sort(key=lambda e: e[2])
        
        mst_weight = 0
        uf = Union(n)

        #original MST
        for v1, v2, weight, i in edges:
            if uf.union(v1, v2):
                mst_weight += weight #ensure MST and if cycle found, skip
        
        critical, pseudo = [], []
        for n1, n2, e_w, i in edges:
            #Try without cur edge for critical
            uf = Union(n)
            weight = 0
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
                #not connected and more expensive    
            if max(uf.rank) != n or weight > mst_weight: 
                critical.append(i)
                continue

            #Try cur edge for pseudo
            uf = Union(n)
            weight = e_w
            uf.union(n1, n2)
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)

        return [critical, pseudo]


            

