class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0 : 1} #base case: choose nothing

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0) #to avoid negative value and get key-value
        return dp[target]