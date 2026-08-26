class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i, j):
            #if they both reach at its end, t end should be check first.
            #successfully formed all of t
            if j == len(t): #s = a and t = "", a canbe removed
                return 1
            #s end before t
            if i == len(s): #s = "", t = a not possible
                return 0
            if (i, j) in dp:
                return dp[(i,j)]

            if s[i] == t[j]:
                dp[(i, j)]= dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i, j)] = dfs(i + 1, j)
            return dp[(i, j)]
        return dfs(0,0)