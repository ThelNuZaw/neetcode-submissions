class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, v):
        if self.par[v] != v:
            self.par[v] = self.find(self.par[v])
        return self.par[v]

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return 
        if self.size[p1] > self.size[p2]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        factor_index = {} # f-> index of value with f
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i
        return uf.count == 1

        