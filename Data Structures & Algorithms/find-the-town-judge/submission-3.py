class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # incoming = defaultdict(int)
        # outcoming = defaultdict(int)

        # for s, d in trust:
        #     incoming[d] += 1
        #     outcoming[s] += 1

        # for i in range(1, n+1):
        #     if incoming[i] == n - 1 and outcoming[i] == 0:
        #         return i
        # return -1

        delta = defaultdict(int) #incoming - outcoming = n - 1 - 0

        for s, d in trust:
            delta[s] -= 1
            delta[d] += 1

        for i in range(1, n + 1):
            if delta[i] == n - 1:
                return i
        return -1