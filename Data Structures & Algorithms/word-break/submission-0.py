class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True #base case

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i : i + len(w)] == w):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break 
                #once one substring is word in wordDict, stop checking the rest and check another index.
        return dp[0]