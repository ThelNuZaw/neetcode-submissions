class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        return False
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailtoacc = {} #email to index of account

        for i, a in enumerate(accounts):
            for e in a[1:]: #to get emails
                if e in emailtoacc:
                    uf.union(i, emailtoacc[e])
                else:
                    emailtoacc[e] = i

        emailgp = defaultdict(list) # grouping emails to merged indices of acc
        for e, i in emailtoacc.items():
            leader = uf.find(i)
            emailgp[leader].append(e)

        res = []
        #sort email and append it to the account name
        for i, e in emailgp.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailgp[i]))
        return res
