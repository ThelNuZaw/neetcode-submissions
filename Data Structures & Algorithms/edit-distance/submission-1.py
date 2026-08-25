class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2)+ 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2) + 1): #bottom row
            dp[len(word1)][j] = len(word2) - j #word1 empty and word2 is string
        for i in range(len(word1) + 1): #last column
            dp[i][len(word2)] = len(word1) - i #word1 is string and word2 is empty

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1] #diagonally
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])#delete/ insert/ replace
        return dp[0][0]