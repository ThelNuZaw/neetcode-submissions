class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1, n + 1): #1 to 13
            for s in range(1, target + 1): # to make this target, need this squares
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        return dp[n]