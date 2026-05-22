class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        f = [[] for _ in range(len(nums)+ 1)] # [[],[],[],...]
        for n in nums:
            d[n] = 1 + d.get(n,0) #{number:frequency}

        for ke, v in d.items(): #frequency = index v / list of # with freq = value k
            f[v].append(ke) 
        
        r = []
        for i in range(len(f) - 1, 0, -1):
            for ke in f[i]:
                r.append(ke)
            if len(r) == k:
                return r    