class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # [8,8,8,..] 
        dp[0] = 0 # if amount = 0, the way to sum up is 0 according to the coins 
        
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin]) # dp[1] = min(8, dp[0]) = 1
        return dp[amount] if dp[amount] != amount + 1 else -1